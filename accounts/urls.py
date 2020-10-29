from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="app-home"),
    path('events/', views.events, name="app-events"),
    path('people/', views.people, name="app-people"),
    path('search/', views.search, name="app-search"),
]