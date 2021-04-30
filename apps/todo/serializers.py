from rest_framework import serializers

from apps.todo.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'notes', 'category', 'priority', 'schedule', 'done']
