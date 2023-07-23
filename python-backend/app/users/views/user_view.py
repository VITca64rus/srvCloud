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


    def post(self, request):
        '''Add or update user'''
        add_user = {
            'tg_id': request.data.get('tg_id'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'username': request.data.get('username')
        }
        print(add_user)
        user = USERS.objects.filter(tg_id=add_user['tg_id']).first()
        if user is not None:
            user.first_name = add_user['first_name']
            user.last_name = add_user['last_name']
            user.username = add_user['username']
            user.save()
            info = f"{add_user['username']} updated in BD"
        else:
            USERS.objects.create(**add_user)
            info = f"{add_user['username']} add to BD"
        return Response({
            'status': 'ok',
            'info': info
        }, status=200)
