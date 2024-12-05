from django.db import models


class CV(models.Model):
    cid = models.CharField(primary_key=True,max_length=10)
    cname = models.CharField(max_length=10)
    tname = models.CharField(max_length=10)
