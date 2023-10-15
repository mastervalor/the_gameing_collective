import bcrypt
from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from django.contrib import messages
from .models import Users, Devices
import json


def index(request):
    return render(request, "login_create.html")

def account_creation(request):
    errors = Users.objects.default_user_validator(request.POST)
    if len(errors) > 0:
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/account/user/create')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
        new_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        try:
            for key in request.session.keys():
                del request.session[key]
        except KeyError:
            print('no sessions')
        except RuntimeError:
            print('no session')
        request.session['user_id'] = new_user.id
        return redirect('/account/finalize')
    
def login(request):
    user = Users.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/')
        messages.warning(request, "This password doesn't match")
        request.session['user_id'] = user.id
        return redirect('/account')

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
        return redirect('/account')
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
