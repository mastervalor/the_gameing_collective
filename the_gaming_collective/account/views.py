from django.shortcuts import render
from general.igdb_api import igdb_api
import json

# Create your views here.

def index(request):
    request.session.flush()
    test = igdb_api.api_get_image_id()
    print(test)
    y = json.loads(test)
    print(y[0]['cover'])
    x = y[0]['cover']
    print(x['image_id'])
    context = {
        "image_id": x['image_id'],
        "site_url": "https://images.igdb.com/igdb/image/upload/t_1080p/",
        "format": ".jpg"
    }
    return render(request, "account_index.html", context)