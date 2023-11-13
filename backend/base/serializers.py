from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email'] # or ['name','_id'] or exclude = ['name','_id']

    def get_name(self,obj):
        name = obj.first_name
        if name=='':
            name=obj.email

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # or ['name','_id'] or exclude = ['name','_id']