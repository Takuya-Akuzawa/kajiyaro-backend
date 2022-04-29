from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# カスタムユーザを定義
class User(AbstractUser):
    pass

    class Meta:
        db_table = 'users'


class Category(models.Model):

    category = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.category
    
    class Meta:
        db_table = 'categories'


class Housework(models.Model):

    housework_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='houseworks', on_delete=models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    estimated_time = models.IntegerField()
    create_user = models.ForeignKey(User, related_name='houseworks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + " - " + self.housework_name

    class Meta:
        db_table = 'houseworks'