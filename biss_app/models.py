from django.db import models


class History(models.Model):
    req = models.IntegerField(null=True)
    res = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
