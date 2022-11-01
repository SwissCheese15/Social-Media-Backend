from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["is_active", "is_staff", "date_joined", "groups", "user_permissions", "last_login", "is_superuser", "is_following"]


class RepresentationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "last_login", "is_superuser", "is_active", "date_joined", "groups", "user_permissions"]


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined", "groups", "user_permissions"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_following'] = RepresentationUserSerializer(instance.is_following, many=True).data
        return representation


class OnlyFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_following"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['is_following'] = RepresentationUserSerializer(instance.is_following, many=True).data
        return representation


