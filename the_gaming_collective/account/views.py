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
        return redirect('/')
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
        return redirect('/finalize')
    
def login(request):
    user = Users.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/homepage')
        messages.warning(request, "This password doesn't match")
        return redirect('/')

def finalize_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    devices = Devices.objects.all()
    return render(request, 'account_finalize.html', {"devices": devices})

def finalize_account(request):
    errors = Users.objects.finalize_user_validator(request.POST)
    if len(errors) > 0:
        request.session['username'] = request.POST['username']
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/finalize')
    else:
        try:
            for key in request.session.keys():
                del request.session[key]
        except KeyError:
            print('no sessions')
        except RuntimeError:
            print('no session')
    user = Users.objects.get(id=request.session['user_id'])
    user.fav_devices = request.POST['devices']
    user.save()
    return redirect('/homepage')

def edit_account(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'edit_account.html')
