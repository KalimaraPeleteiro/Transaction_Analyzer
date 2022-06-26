from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload', views.upload, name='upload'),
    path('newfile', views.newfile, name='newfile'),
    path('history', views.history, name='history'),
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]
