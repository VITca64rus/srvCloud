'''serializers for app vpn'''
from rest_framework import serializers
from servers.models.server_model import SERVERS
from servers.serializers import ServersSerializer
from users.models.user_model import USERS
from users.serializers import UsersSerializer
from vpn.models.vpn_model import VPNS


class VPNSSerializer(serializers.ModelSerializer):
    '''Serializer for table vpns'''
    user = serializers.SerializerMethodField(required=False)
    server = serializers.SerializerMethodField(required=False)

    def get_user(self, obj):
        '''Return user'''
        users_set = USERS.objects.filter(tg_id=obj.user_id)
        if users_set:
            users_set = UsersSerializer(users_set, many=False)
            return users_set.data
        else:
            return None

    def get_server(self, obj):
        '''Return server'''
        servers_set = SERVERS.objects.filter(id=obj.server_id)
        if servers_set:
            servers_set = ServersSerializer(servers_set, many=False)
            return servers_set.data
        else:
            return None

    class Meta:
        '''meta for choise fields'''
        model = VPNS
        fields = ('id', 'server', 'user', 'started_at', 'finished_at')
