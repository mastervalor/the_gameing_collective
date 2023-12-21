import bcrypt
from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Users, Devices
import json


def index(request):
    return render(request, "login_create.html")

def logout_view(request):
    logout(request)
    return redirect('/')

def account_creation(request):
    if request.method == 'POST':
        errors = Users.objects.default_user_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, "account_creation.html", {
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'email': request.POST['email']
            })
        else:
            try:
                user = User.objects.create_user(username=request.POST['email'], 
                                                email=request.POST['email'], 
                                                password=request.POST['password'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'])
                login(request, user)  # Log in the newly created user
                return redirect('/account/finalize')
            except Exception as e:
                messages.error(request, str(e))
                return render(request, "account_creation.html", {
                    'first_name': request.POST['first_name'],
                    'last_name': request.POST['last_name'],
                    'email': request.POST['email']
                })
    else:
        return render(request, "account_creation.html")
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid email or password")
    return render(request, "login_create.html")

def finalize_page(request):
    if 'user_id' not in request.session:
        return redirect('/account')
    devices = Devices.objects.all()
    return render(request, 'account_finalize.html', {"devices": devices})

def finalize_account(request):
    errors = Users.objects.finalize_user_validator(request.POST)
    if len(errors) > 0:
        request.session['username'] = request.POST['username']
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/account/finalize')
    else:
        try:
            for key in request.session.keys():
                del request.session[key]
        except KeyError:
            print('no sessions')
        except RuntimeError:
            print('no session')
    user = Users.objects.get(id=request.session['user_id'])
    print(f"this is what your looking for {request.POST}")
    user.fav_devices.set(request.POST['devices'])
    user.save()
    return redirect('/')

def edit_account(request):
    if 'user_id' not in request.session:
        return redirect('/account/login_create')
    user = Users.objects.get(id=request.session['user_id'])
    devices = Devices.objects.all()
    return render(request, 'edit_account.html', {'user': user, "devices": devices})

def delete_account(request):
    Users.objects.get(id=request.session['user_id']).delete()
    return redirect('/account')

def update_account(request):
    errors = Users.objects.edit_user_validator(request.POST)
    if len(errors) > 0:
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        request.session['username'] = request.POST['username']
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/account/edit_account')
    else:
        user = Users.objects.get(id=request.session['user_id'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['username']
        user.fav_dev = request.POST['devices']
        user.save()
        try:
            for key in request.session.keys():
                del request.session[key]
        except KeyError:
            print('no sessions')
        except RuntimeError:
            print('no session')
    return redirect('/')
