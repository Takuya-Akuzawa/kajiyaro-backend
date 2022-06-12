from dataclasses import field
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework import serializers
from .models import Task, User, Category, Housework


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True, 'min_length': 8}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'category_name',
        )


class HouseworkSerializer(serializers.ModelSerializer):

    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    create_user = PrimaryKeyRelatedField(queryset=User.objects.all())
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
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['category'] = CategorySerializer(context=self.context).to_representation(instance.category)
        ret['create_user'] = UserSerializer(context=self.context).to_representation(instance.create_user)
        return ret

    
class TaskSerializer(serializers.ModelSerializer):

    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    assigned_user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = (
            'id',
            'task_name',
            'category',
            'status',
            'assigned_user',
            'scheduled_date',
            'result_date',
            'result_time',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['category'] = CategorySerializer(context=self.context).to_representation(instance.category)
        ret['assigned_user'] = UserSerializer(context=self.context).to_representation(instance.assigned_user)
        return ret

    