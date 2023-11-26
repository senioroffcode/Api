from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import *
from .serializer import *

@api_view(['GET'])
def get_task_view(request):
    query = Task.objects.all()
    serializer.date = TaskSerializer(query, many=True).date
    print(serializer_data)
    return Response()