from django.db.models import Q
from django.shortcuts import render

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Game


def slot_view(request):
    # games = Game.objects.all()
    games = Game.objects.filter(type='SLOT')
    paginator = Paginator(games, 6)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'slot.html', {'page_obj': page_obj, 'games': page_obj})


def game_search_view(request):
    query = request.GET.get('q')
    games = Game.objects.all()
    page_number = request.GET.get('page')

    if query:
        games = games.filter(name__icontains=query)

    paginator = Paginator(games, 6)
    paginator.count = games.count()  # Update paginator count with the filtered game count

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'game_search.html', {'page_obj': page_obj, 'games': page_obj, 'query': query})
    # return render(request, 'game_search.html', {'page_obj': page_obj, 'games': games, 'query': query})



from django.shortcuts import render, get_object_or_404
from .models import Game


def game_detail_view(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game_detail1.html', {'game': game})


def home_view(request):
    return render(request, 'newhome.html')


def ETG_view(request):
    # games = Game.objects.all()
    games = Game.objects.filter(type='ETG')
    paginator = Paginator(games, 6)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'ETG.html', {'page_obj': page_obj, 'games': page_obj})


def about_view(request):

    return render(request, 'about.html')