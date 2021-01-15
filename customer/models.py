from django.db import models

# Create your models here.

class member_db(models.Model):
    name=models.CharField(max_length=10, verbose_name="name")
    passwd=models.CharField(max_length=10, verbose_name="pw")
