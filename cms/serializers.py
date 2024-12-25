# cms/serializers.py
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import SystemInfo, Article, CustomPage, Tag, Category, UserProfile


class SystemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInfo
        fields = ['id', 'name', 'description', 'seo_title', 'seo_description', 'seo_keywords']

class CustomPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPage
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    is_staff = serializers.BooleanField(required=False, default=False)
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'is_staff', 'profile_picture')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_staff=validated_data.get('is_staff', False)
        )

        user.set_password(validated_data['password'])
        user.save()

        if profile_picture:
            UserProfile.objects.create(user=user, profile_picture=profile_picture)
        else:
            UserProfile.objects.create(user=user)

        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'profile_picture')
        read_only_fields = ('is_staff',)  # 仅管理员可以修改is_staff字段

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile_picture', None)
        user = super().update(instance, validated_data)

        if profile_data:
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.profile_picture = profile_data
            user_profile.save()

        return user

class UserDetailSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'profile')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'cover', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def create(self, validated_data):
        # 自动设置作者为当前登录用户
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)