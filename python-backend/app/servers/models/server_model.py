'''Models for app servers'''
from django.db import models


class SERVERS(models.Model):
    '''Table for servers'''
    ip = models.CharField(max_length=16)
    ptr = models.CharField(max_length=200)
