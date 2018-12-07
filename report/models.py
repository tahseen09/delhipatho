from django.db import models

# Create your models here.
class query(models.Model):
    id=models.IntegerField(primary_key=True)
    name1=models.CharField(max_length=30, null=True, blank = True)
    repo1=models.FileField(upload_to='documents/',null=True, blank=True)
    name2=models.CharField(max_length=30, null=True, blank = True)
    repo2=models.FileField(upload_to='documents/',null=True, blank=True)
    name3=models.CharField(max_length=30, null=True, blank = True)
    repo3=models.FileField(upload_to='documents/',null=True, blank=True)

