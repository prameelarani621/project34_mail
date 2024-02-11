from typing import Any
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class userprofilemanager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password:None):
        if not email:
            raise ValueError('provide email')

        ne=self.normalize_email(email)
        UPO=self.model(email=ne,first_name=first_name,last_name=last_name)
        UPO.set_password(password)
        UPO.save()
        return UPO
    
    def create_superuser(self,email,first_name,last_name,password):
        UPO=self.create_user(email,first_name,last_name,password)
        UPO.is_superuser=True
        UPO.is_staff=True
        UPO.save()

class userprofile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=userprofilemanager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    def __str__(self):
        return self.first_name+''+self.last_name