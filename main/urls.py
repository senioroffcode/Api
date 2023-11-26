from django.urls import path
from .views import *

urlpatterns = [
   path("get-tasks/", get_task_view)
]
