from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload', views.upload, name='upload'),
    path('newfile', views.newfile, name='newfile'),
    path('history', views.history, name='history'),
    path('<int:operation_id>', views.operation, name='operation'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
]
