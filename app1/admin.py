from django.contrib import admin
from .models import CustomUser,Profile,Post,Comment
admin.site.register(CustomUser)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)

