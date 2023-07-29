'''general view for app vpn'''
from django.core.paginator import Paginator
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from vpn.models.vpn_model import SUBSCRIPTIONS, VPNS
from vpn.serializers import SubscriptionsSerializer, VpnsSerializer


class VPN(APIView):
    '''Class for manage VPN'''
    def get(self, request):
        '''Return info VPN'''
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        mode = request.GET.get('mode')
        if mode == 'get_subscriptions':
            subscriptions_set = SUBSCRIPTIONS.objects.all()
            subscriptions_set = self._filter_subscriptions(subscriptions_set, request)
            total_records = subscriptions_set.count()
            paginator = Paginator(subscriptions_set, limit)
            subscriptions_set = paginator.get_page(page)
            users = SubscriptionsSerializer(subscriptions_set, many=True)
            return Response({
                'total_records': total_records,
                'data': users.data
            }, status=200)
        elif mode == 'get_vpns':
            vpns_set = VPNS.objects.all()
            vpns_set = self._filter_vpns(vpns_set, request)
            total_records = vpns_set.count()
            paginator = Paginator(vpns_set, limit)
            vpns_set = paginator.get_page(page)
            users = VpnsSerializer(vpns_set, many=True)
            return Response({
                'total_records': total_records,
                'data': users.data
            }, status=200)
        else:
            return Response({
                'info': 'bad mode'
            }, status=400)

    def _filter_vpns(self, queryset, request):
        '''Filters products vpn'''
        filters = {
            'id': request.GET.getlist('filter_id[]') or [request.GET.get('filter_id')],
            'payload': request.GET.getlist('filter_payload[]') or [request.GET.get('filter_payload')],
        }
        if filters['id'][0]:
            queryset = queryset.filter(id__in=filters['id'])
        if filters['payload'][0]:
            queryset = queryset.filter(payload__in=filters['payload'])
        return queryset

    def _filter_subscriptions(self, queryset, request):
        '''Filters subscriptions'''
        filters = {
            'id': request.GET.getlist('filter_id[]') or [request.GET.get('filter_id')],
            'payload': request.GET.getlist('filter_payload[]') or [request.GET.get('filter_payload')],
            'active': request.GET.get('filter_active'),
        }
        if filters['id'][0]:
            queryset = queryset.filter(id__in=filters['id'])
        if filters['payload'][0]:
            queryset = queryset.filter(product__payload__in=filters['payload'])
        if filters['active']:
            current_time = timezone.now()
            if filters['active'] == 'true':
                queryset = queryset.filter(finished_at__gt=current_time)
            else:
                queryset = queryset.filter(finished_at__lt=current_time)
        return queryset
