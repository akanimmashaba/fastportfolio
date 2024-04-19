from django.urls import path

from portfolio.views import index,projects,connect

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
    path('connect/', connect, name='connect')
    
]