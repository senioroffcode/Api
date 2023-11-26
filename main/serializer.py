from rest_framework import serializer
from .models import *

class TaskSerializer(serializer.ModalSerializer):
    class Meta:
        models = Task
        fields = 'id',name