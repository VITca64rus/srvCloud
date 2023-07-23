'''models for app users'''
from django.db import models


class USERS(models.Model):
    '''Table for users'''
    tg_id = models.CharField(max_length=200, primary_key=True)
    tg_link = models.CharField(max_length=200)
    tg_name = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
