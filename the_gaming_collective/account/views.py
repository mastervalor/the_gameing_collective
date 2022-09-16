from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
import json

# Create your views here.

def index(request):
    return render(request, "login_create.html")

def account_creation(request):
    return redirect("/finalize")

def finalize(request):
    return render(request, 'account_finalize.html')
