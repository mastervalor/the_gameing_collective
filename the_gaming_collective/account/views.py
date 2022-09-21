from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from django.contrib import messages
from .models import Users
import json

# Create your views here.

def index(request):
            return render(request, "login_create.html")

def account_creation(request):
    errors = Users.objects.default_user_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        try:
            for key in request.session.keys():
                del request.session[key]
        except KeyError:
            print('no sessions')
        new_user = Users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        request.session['user_id'] = new_user.id
        return redirect('finalize')
        

def finalize(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print(request.POST['platforms'])
    user = Users.objects.get(id=request.session['user_id'])
    # user.plat
    return render(request, 'account_finalize.html')
