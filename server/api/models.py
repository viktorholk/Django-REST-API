from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_verified=True, is_active=True, is_staff=False):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have a email')
        if not password:
            raise ValueError('Users must have a password')
        # Create model
        user = self.model(
            username    = username,
            email       = email,
            active   = is_active,
            staff    = is_staff
        )
        # Set password and save the user in the database
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password,
            is_staff=True
        )
        return user

class User(AbstractBaseUser):
    # User info
    email       = models.EmailField(max_length=255, unique=True, db_index=True)
    username    = models.CharField(max_length=35, unique=True, db_index=True)
    # Boolean s
    verified = models.BooleanField(default=False)
    active   = models.BooleanField(default=True)
    staff    = models.BooleanField(default=False)

    # Dates
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return self.staff

    def has_module_perms(self, app_label):
        return self.staff