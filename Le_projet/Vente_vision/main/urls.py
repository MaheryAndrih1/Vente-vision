from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('Accueil',views.accueil, name='Accueil'),
    path('',views.accueil, name='Accueil'),
    path('home',views.home, name='home'),
    path('sign-up',views.sign_up, name='sign-up'),
    path('create-post',views.create_post, name='create-post'),
    path('show-cli', views.client_show, name='show-cli') #the test (deletable)
]