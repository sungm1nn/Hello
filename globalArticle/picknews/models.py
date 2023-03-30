from django.db import models

# Create your models here.
class user_subs(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True, null=False)
    keyword = models.CharField(max_length=50, null=False)
    per = models.CharField(max_length=100, null=False)
    nation = models.CharField(max_length=200 ,null=False) 
    frequency = models.IntegerField()
    none_check = models.BooleanField(default=False)