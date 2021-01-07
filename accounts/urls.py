from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="app-home"),
    path('events/', views.events, name="app-events"),
    path('people/', views.people, name="app-people"),
    path('search/', views.search, name="app-search"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)