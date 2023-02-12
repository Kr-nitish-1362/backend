from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, email=None, username=None, password=None,     **extra_fields):
        if email:
            email = self.normalize_email(email)
        
        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extra_fields
        )
        user.is_active = True
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email, username=username, **extra_fields
            )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to = 'uploads/images/profile_images', null=True, blank=True)
    address = models.CharField(max_length=510, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False) # for admin login
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = UserAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
