'''Serializers for app servers'''
from rest_framework import serializers
from servers.models.server_model import SERVERS


class ServersSerializer(serializers.ModelSerializer):
    '''Serializer for table servers'''
    class Meta:
        '''meta for choise fields'''
        model = SERVERS
        fields = ('__all__',)
