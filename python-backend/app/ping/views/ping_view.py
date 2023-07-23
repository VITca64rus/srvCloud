from rest_framework.response import Response
from rest_framework.views import APIView


class Ping(APIView):
    '''Class for check status DRF'''
    def get(self, request):
        '''Health check'''
        return Response("pong")
