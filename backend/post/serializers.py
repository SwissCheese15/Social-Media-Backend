from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import Post
from user.serializers import UserSerializer, RepresentationUserSerializer

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = RepresentationUserSerializer(instance.owner, many=False).data
        return representation


class NewPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ["is_liked_by"]


class TogglePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "is_liked_by"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = UserSerializer(instance.owner, many=False).data["username"]
        return representation