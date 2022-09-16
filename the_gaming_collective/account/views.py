from django.shortcuts import render
from general.igdb_api import igdb_api
import json

# Create your views here.

def index(request):
    request.session.flush()
    test = igdb_api.api_get_image_id()
    print(test)
    y = json.loads(test)
    print(y)
    print(y[0]['name'])
    print(y[0]['release_dates'][0]['human'])
    
    return render(request, "account_index.html", {'list': y})