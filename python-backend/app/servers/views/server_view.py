'''Models for app servers'''
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from servers.models.server_model import SERVERS
from servers.serializers import ServersSerializer


class Server(APIView):
    '''Class for manage Server'''
    def get(self, request):
        '''Return the servers'''
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        servers_set = SERVERS.objects.all()
        total_records = servers_set.count()
        paginator = Paginator(servers_set, limit)
        servers_set = paginator.get_page(page)
        servers = ServersSerializer(servers_set, many=True)
        return Response({
            'total_records': total_records,
            'servers': servers.data
        }, status=200)
