'''urls for app servers'''
from django.urls import path
from servers.views import server_view


urlpatterns = [
    path('servers/', server_view.Server.as_view())
]
