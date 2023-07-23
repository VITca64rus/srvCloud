'''models for app vpns'''
from django.db import models
from users.models.user_model import USERS
from servers.models.server_model import SERVERS


class VPNS(models.Model):
    '''Table for vpns info'''
    server_id = models.ForeignKey(to=SERVERS, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=USERS, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        '''Init indexes'''
        indexes = [
            models.Index(fields=['finished_at'])
        ]
