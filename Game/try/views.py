from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Game


def home_view(request):
    games = Game.objects.all()
    paginator = Paginator(games, 5)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'home.html', {'page_obj': page_obj, 'games': games}, )