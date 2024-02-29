from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self,username,email,password,firstname=None,lastname=None,**extra_fields):
        if not username:
            raise ValueError('Username must be provided')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,is_staff=extra_fields['is_staff'],is_superuser=extra_fields['is_superuser'])
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password,**extra_fields)
    
class Station(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50,unique=True,)
    email = models.CharField(max_length=30)
    is_superuser = models.BooleanField(null=True)
    is_staff = models.BooleanField(null=True)
    station = models.ForeignKey(Station,on_delete=models.CASCADE,null=True,blank=True)
    firstname = models.CharField(max_length = 30,null=True,blank=True)
    lastname = models.CharField(max_length = 30,null=True,blank=True)
    objects = UserManager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email',]
    
    def __str__(self):
        return self.username



class FoundId(models.Model):
    id_no = models.CharField(max_length= 10,primary_key = True)
    date_found = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    station = models.ForeignKey(Station,on_delete=models.CASCADE,null=True,blank=True)
    picked = models.BooleanField(default = False)
    
    def __str__(self):
        return self.id_no
    
class Searching(models.Model):
    id_no = models.CharField(max_length= 10,primary_key = True)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 14)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.id_no