from django.urls import path

from . import views

app_name = 'portfolioPage'

urlpatterns = [
    path('', views.base, name='base')
]