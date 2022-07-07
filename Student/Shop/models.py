from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    no_of_worker = models.IntegerField()
    email = models.EmailField()
