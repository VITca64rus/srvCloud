'''general view for app users'''
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models.user_model import USERS
from users.serializers import UsersSerializer


class User(APIView):
    '''Class for manage User'''
    def get(self, request):
        '''Return users'''
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        users_set = USERS.objects.all()
        total_records = users_set.count()
        paginator = Paginator(users_set, limit)
        users_set = paginator.get_page(page)
        users = UsersSerializer(users_set, many=True)
        return Response({
            'total_records': total_records,
            'servers': users.data
        }, status=200)
