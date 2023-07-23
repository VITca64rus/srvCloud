'''Serializers for app users'''
from rest_framework import serializers
from users.models.user_model import USERS


class UsersSerializer(serializers.ModelSerializer):
    '''Serializer for table users'''
    class Meta:
        '''meta for choise fields'''
        model = USERS
        fields = ('tg_id', 'first_name', 'last_name', 'username')
