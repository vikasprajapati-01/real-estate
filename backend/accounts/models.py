from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager) :
    def create_user(self, name, email, password= None):
        if not email:
            raise ValueError('Email must be entered')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save()

        return user

# Model for the users data
class UserAccount(AbstractBaseUser , PermissionsMixin) :
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email