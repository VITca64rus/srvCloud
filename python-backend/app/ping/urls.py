'''urls for app ping'''
from django.urls import path
from ping.views import ping_view


urlpatterns = [
    path('ping/', ping_view.Ping.as_view())
]
