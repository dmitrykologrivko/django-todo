from rest_framework import serializers

from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'description', 'is_done', 'user', 'created', 'updated')
        read_only_fields = ('user',)
