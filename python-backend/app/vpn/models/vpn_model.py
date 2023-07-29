'''models for app vpns'''
from django.db import models
from users.models.user_model import USERS
from servers.models.server_model import SERVERS


class VPNS(models.Model):
    '''Table for product vpn'''
    name = models.CharField(max_length=200)
    server = models.ForeignKey(to=SERVERS, on_delete=models.CASCADE)
    description = models.TextField()
    payload = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    price_label = models.CharField(max_length=50)
    price_amount = models.IntegerField()


class SUBSCRIPTIONS(models.Model):
    '''Table for subscriptions info'''
    user_id = models.ForeignKey(to=USERS, on_delete=models.CASCADE)
    product = models.ForeignKey(to=VPNS, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        '''Init indexes'''
        indexes = [
            models.Index(fields=['finished_at'])
        ]
