from django.db import models


class History(models.Model):
    """
    Stores all entries, related to :model:`biss_app.History`
    """
    req = models.IntegerField(null=True)
    res = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
