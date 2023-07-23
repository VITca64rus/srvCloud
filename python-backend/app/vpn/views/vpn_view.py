'''general view for app vpn'''
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from vpn.models.vpn_model import VPNS
from vpn.serializers import VPNSSerializer


class VPN(APIView):
    '''Class for manage VPN'''
    def get(self, request):
        '''Return info VPN'''
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        vpns_set = VPNS.objects.all()
        total_records = vpns_set.count()
        paginator = Paginator(vpns_set, limit)
        vpns_set = paginator.get_page(page)
        users = VPNSSerializer(vpns_set, many=True)
        return Response({
            'total_records': total_records,
            'servers': users.data
        }, status=200)
