from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from django.db.models.signals import post_save
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('instructor', 'instructor'),
        ('person', 'Someone who wants treatment'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='normal_user')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    typee = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    experience = models.TextField()
    certificates = models.TextField()


class Post(models.Model):
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)