from django.db import models

# Create your models here.
class Charity(models.Model):

    name = models.CharField(max_length=80)
    yearlydonation = models.CharField(max_length=40)
    email = models.EmailField(max_length=45)
    phone = models.CharField(max_length=30)
    volunteer = models.CharField(max_length=15)





