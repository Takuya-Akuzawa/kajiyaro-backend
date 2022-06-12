from asyncio import Task
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, User, Housework, Task


# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Housework)
admin.site.register(Category)
admin.site.register(Task)