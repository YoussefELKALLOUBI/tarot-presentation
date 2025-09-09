from django.urls import path
from . import views

app_name = 'presentation'

urlpatterns = [
    path('', views.home, name='home'),
    path('sites/', views.sites_overview, name='sites'),
    path('mission/', views.mission, name='mission'),
    path('pyros/', views.pyros_software, name='pyros'),
    path('contact/', views.contact, name='contact'),
]