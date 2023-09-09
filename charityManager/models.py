from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NgoMaster(models.Model):
    ngo_name =models.OneToOneField(User, on_delete=models.CASCADE)
    ngo_phone = models.CharField(max_length=512)
    ngo_city = models.CharField(max_length=512)
    ngo_state = models.CharField(max_length=512)
    ngo_fund = models.IntegerField(default=0)
    
class CharityType(models.Model):
    name = models.CharField(max_length=512)
    desc = models.CharField(max_length=512)
    
class NgoType(models.Model):
    ngo = models.ForeignKey(NgoMaster, on_delete=models.CASCADE)
    ngo_type = models.ForeignKey(CharityType, on_delete=models.CASCADE)
    
class UserMaster(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=512)
    user_wallet = models.IntegerField(default=0)

class UserPref(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_pref = models.ForeignKey(CharityType, on_delete=models.CASCADE)
    
    
# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)