'''models for app users'''
from django.db import models


class USERS(models.Model):
    '''Table for users'''
    tg_id = models.CharField(max_length=200, primary_key=True)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
