from rest_framework import serializers
from .models import User, Category, Housework


# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'category',
        )


class HouseworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housework
        fields = (
            'id', 
            'housework_name',
            'category',
            'description',
            'estimated_time',
            'create_user',
        )
        
