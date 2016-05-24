from __future__ import unicode_literals

from django.db import models

class Somebody(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField(null=True, blank=True)
    BIO = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
