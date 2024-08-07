from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    status = serializers.ChoiceField(choices=Task.STATUSES)

    class Meta:

        model = Task
        fields = ['id', 'name', 'description', 'status']