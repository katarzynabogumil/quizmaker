from rest_framework import serializers

from .models import User, Quiz, Question, Score


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


class QuizSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "author",
            "title",
            "description",
            "timestamp",
            "public",
            "colour_class",
        ]
