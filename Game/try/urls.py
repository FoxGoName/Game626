from django.urls import path
from .views import home_view, game_search_view, game_detail_view, slot_view, ETG_view, about_view


urlpatterns = [

    path('slot', slot_view, name='slot'),
    path('', home_view, name='home'),
    path('ETG', ETG_view, name='ETG'),
    path('about', about_view, name='about'),
    path('<int:game_id>', game_detail_view, name='game_detail'),
    path('games/search/', game_search_view, name='game_search'),
]