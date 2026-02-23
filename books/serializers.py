# from rest_framework import serializers
# from .models import Book
# from django.contrib.auth.models import User

# class AuthorSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     class Meta:
#         model = User
#         fields = ['username','password','email']

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         queryset = User.objects.all(),
#         slug_field = 'username'
#     )
#     author_details = AuthorSerializer(source="author",read_only=True)

#     class Meta:
#         model = Book
#         fields = '__all__'

#     def validate_title(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Title is too short")
#         return value
    
#     def validate(self,data):
#         year = data.get('published_year')

#         if year and year > 2026:
#             raise serializers.ValidationError("Published Year in invalid")
#         return data

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']

class BookSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field = 'username'
    )

    author_details = AuthorSerializer(source="author",read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['created_at']

class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email']

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user