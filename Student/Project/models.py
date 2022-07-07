from unicodedata import name
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    roll_no =models.IntegerField()
    address = models.CharField(max_length=10)
    contact =models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name