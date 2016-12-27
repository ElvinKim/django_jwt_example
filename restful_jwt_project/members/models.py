from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Member(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    last_mod_date = models.DateTimeField(default=datetime.now, blank=True)

