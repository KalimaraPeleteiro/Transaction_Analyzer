from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload', views.upload, name='upload'),
    path('history', views.history, name='history'),
    path('profile', views.profile, name='profile')
]
