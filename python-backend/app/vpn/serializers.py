'''serializers for app vpn'''
from rest_framework import serializers
from servers.models.server_model import SERVERS
from servers.serializers import ServersSerializer
from users.models.user_model import USERS
from users.serializers import UsersSerializer
from vpn.models.vpn_model import VPNS, SUBSCRIPTIONS


class SubscriptionsSerializer(serializers.ModelSerializer):
    '''Serializer for table subscriptions'''
    user = serializers.SerializerMethodField(required=False)
    product = serializers.SerializerMethodField(required=False)

    def get_user(self, obj):
        '''Return user'''
        users_set = USERS.objects.filter(tg_id=obj.user_id).first()
        if users_set:
            users_set = UsersSerializer(users_set, many=False)
            return users_set.data
        else:
            return None

    def get_product(self, obj):
        '''Return product'''
        vpns_set = VPNS.objects.filter(id=obj.product_id).first()
        if vpns_set:
            vpns = VpnsSerializer(vpns_set, many=False)
            return vpns.data
        else:
            return None

    class Meta:
        '''meta for choise fields'''
        model = SUBSCRIPTIONS
        fields = ('id', 'product', 'user', 'started_at', 'finished_at')


class VpnsSerializer(serializers.ModelSerializer):
    '''Serializer for table vpns'''
    server = serializers.SerializerMethodField(required=False)

    def get_server(self, obj):
        '''Return server'''
        servers_set = SERVERS.objects.filter(id=obj.server_id).first()
        if servers_set:
            servers = ServersSerializer(servers_set, many=False)
            return servers.data
        else:
            return None

    class Meta:
        '''meta for choise fields'''
        model = VPNS
        fields = ('id', 'name', 'server', 'description', 'payload',
                  'currency', 'price_label', 'price_amount')
