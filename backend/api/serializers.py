"""Модуль сериализаторов для API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для модели задачи."""

    class Meta:
        """Метаданные сериализатора."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
