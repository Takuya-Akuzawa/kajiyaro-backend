from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework import serializers
from .models import User, Category, Housework


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
            'category',
        )


class HouseworkSerializer(serializers.ModelSerializer):

    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    # username = serializers.ReadOnlyField(source='user.username', read_only=True)
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
        return ret