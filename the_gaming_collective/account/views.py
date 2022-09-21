from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from django.contrib import messages
from .models import Users
import json

# Create your views here.

def index(request):
    errors = Users.objects.default_user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
        else:
            return render(request, "login_create.html")

def account_creation(request):
    
    return redirect("/finalize")

def finalize(request):
    return render(request, 'account_finalize.html')
