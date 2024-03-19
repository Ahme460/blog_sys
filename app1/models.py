from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser , PermissionsMixin
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('instructor', 'instructor'),
        ('person', 'Someone who wants treatment'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='normal_user')
   # email = models.EmailField(max_length=100, unique=True)