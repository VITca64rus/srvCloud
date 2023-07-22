from django.urls import path
from ping.views import PingView


urlpatterns = [
    path('ping/', PingView.Ping.as_view())
]
