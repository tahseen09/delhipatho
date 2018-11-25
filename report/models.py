from django.db import models

# Create your models here.
class query(models.Model):
    id=models.IntegerField(primary_key=True)
    repo=models.FileField(upload_to='documents/')
