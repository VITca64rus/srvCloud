'''urls for app vpn'''
from django.urls import path
from vpn.views import vpn_view


urlpatterns = [
    path('vpn/', vpn_view.VPN.as_view())
]
