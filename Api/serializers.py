from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Category, SubCategory, Product, Cart

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(max_length=5, write_only=True)
    brand_name = serializers.SerializerMethodField()
    
    def validate_price(self, value):
        if value < 100 and value > 1000000:
            raise serializers.ValidationError('Price must be between 100 and 1,000,000.')
        return value
    
    def get_brand_name(self, obj):
        return obj.brand.name

    class Meta:
        model = Product
        fields = ['product_id', 'name', 'slug', 'price', 'category', 'brand', 'brand_name', 'sub_category', 'release_year', 'in_stock']
        read_only_fields = ['slug']


class SubCategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = SubCategory
        fields = ['name', 'slug', 'category', 'products']
        read_only_fields = ['slug']

class CategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)
    sub_categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'sub_categories', 'products']
        read_only_fields = ['slug']

    
class BrandSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Brand
        fields = ['name', 'slug', 'products']
        read_only_fields = ['slug']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'date']
        read_only_fields = ['date']