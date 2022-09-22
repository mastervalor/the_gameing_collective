from operator import ne
from django.shortcuts import render, redirect
from general.igdb_api import igdb_api
from datetime import datetime
from account.models import Users, Devices
from .models import Games, Reviews
import json

# Create your views here.


def index(request):
    
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    # Upcoming PS5 and Xbox Series X|S games (Can be expanded to PC just needs to be worked)
    up_json = igdb_api.api_get_upcoming_games(milliseconds)
    up_games = json.loads(up_json)

    #Game pass games
    gp_json = igdb_api.api_get_game_by_marketplace(54)
    gp_games = json.loads(gp_json)

    #Game xbox market place
    xbm_json = igdb_api.api_get_game_by_marketplace(31)
    xbm_games = json.loads(xbm_json)

    #Game playstation store
    pss_json = igdb_api.api_get_game_by_marketplace(36)
    pss_games = json.loads(pss_json)

    #Game epic store
    epic_json = igdb_api.api_get_game_by_marketplace(26)
    epic_games = json.loads(epic_json)
    
    return render(request, "homepage.html", {'gp_list': gp_games, 'up_list': up_games, 'xbm_list':xbm_games, 'pss_list': pss_games, 'epic_list':epic_games})

def games(request):

    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    # Games by console

    #PS5 games
    ps5_json = igdb_api.api_get_games_by_platform(167, milliseconds)
    ps5_games = json.loads(ps5_json)

    #Xbox series X|S games
    xbox_xs_json = igdb_api.api_get_games_by_platform(169, milliseconds)
    xbox_xs_games = json.loads(xbox_xs_json)

    #PC games
    pc_json = igdb_api.api_get_games_by_platform(6, milliseconds)
    pc_games = json.loads(pc_json)

    #Switch games
    nin_json = igdb_api.api_get_games_by_platform(130, milliseconds)
    nin_games = json.loads(nin_json)

    # doing genre pulls this way because if I try to pull all games there are too many
    # and I'm unable to get a decent list even out of 500 results

    #Adventure games
    adv_json = igdb_api.api_get_games_by_genre(31, milliseconds)
    adv_games = json.loads(adv_json)

    #FPS/TPS games
    fps_json = igdb_api.api_get_games_by_genre(5, milliseconds)
    fps_games = json.loads(fps_json)

    #Fighting games
    fight_json = igdb_api.api_get_games_by_genre(4, milliseconds)
    fight_games = json.loads(fight_json)

    #Racing games
    race_json = igdb_api.api_get_games_by_genre(10, milliseconds)
    race_games = json.loads(race_json)

    #Sport games
    sport_json = igdb_api.api_get_games_by_genre(14, milliseconds)
    sport_games = json.loads(sport_json)
    return render(request, "games_page.html", {'adv_list': adv_games,
    'fps_list': fps_games, 'fight_list': fight_games, 'race_list': race_games, 'sport_list': sport_games,
    'ps5_list': ps5_games, 'xbox_xs_list': xbox_xs_games, 'pc_list': pc_games, 'nin_list': nin_games})

def one_game(request, game_id):

    game_json = igdb_api.api_get_one_game(game_id)
    game = json.loads(game_json)
    
    game_reviews = Reviews.objects.all()

    user_context = {
        'user_id': request.session['user_id']
    }
    return render(request, "one_game.html", {'one_game': game, 'game_reviews': game_reviews, 'user':user_context})

def users_games(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    game_id_set = set()
    count = 0
    all_like = Games.objects.all()
    new_string = "("
    for i in range(len(all_like)):
        test = Games.objects.get(id=i+1)
        game_id_set.add(test.game_api_id)
    print(game_id_set)
    
    for j in game_id_set:
        count += 1 
        new_string += str(j)
        if count < len(game_id_set):
            new_string += ", "
        else:
            new_string += ")"
        
    game_json = igdb_api.api_get_one_game(new_string)
    game_list = json.loads(game_json)

    return render(request, "users_games.html", {'game_list': game_list})

def view_all_platform(request, platform_id):
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    plat_json = igdb_api.api_get_games_by_platform_extended(platform_id, milliseconds)
    plat_games = json.loads(plat_json)

    return render(request, "view_all_plat.html", {'plat_list': plat_games})

def view_all_genre(request, genre_id):
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    genre_json = igdb_api.api_get_games_by_genre_extended(genre_id, milliseconds)
    genre_games = json.loads(genre_json)

    return render(request, "view_all_genre.html", {'genre_list': genre_games})

def view_all_marketplace(request, marketplace_id):
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    milliseconds = round(seconds * 1000)

    mrkt_json = igdb_api.api_get_game_by_marketplace_extended(marketplace_id, milliseconds)
    mrkt_games = json.loads(mrkt_json)

    return render(request, "view_all_marketplace.html", {'mrkt_list': mrkt_games})

def review_game(request, game_id):
    game_json = igdb_api.api_get_one_game(game_id)
    game = json.loads(game_json)
    return render(request, "review_page.html", {'one_game': game})

def submit_review(request, game_id):

    review_from_form = request.POST['review']
    score_from_form = float(request.POST['review_score'])

    newly_created_review = Reviews(review = review_from_form, score = score_from_form, game_api_id = game_id)
    newly_created_review.save()

    return redirect(f"/games/{game_id}", {'newly_created_review': newly_created_review})

def search(request):
    search_from_form = request.POST['search_name']
    print(search_from_form)
    search_json = igdb_api.api_search_game_by_name(search_from_form)
    search_results = json.loads(search_json)
    return render(request, "search_results_page.html", {'search_list': search_results})

def likes(request, game_id):
    user = Users.objects.get(id = request.session['user_id'])
    new_like = Games(game_api_id = game_id)
    new_like.save()
    new_like.fav_games.add(user)
    return redirect(f"/games/your_games/{request.session['user_id']}", {'new_like': new_like})
