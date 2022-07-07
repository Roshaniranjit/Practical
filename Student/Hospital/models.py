from django.db import models

class Hospital(models.Model):
    ward_no =models.IntegerField()
    bed_no =models.IntegerField()
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.address