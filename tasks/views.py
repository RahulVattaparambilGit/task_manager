from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'Completed'
        task.save()
        return Response({'status': 'Task completed'})
    

def index(request):
    return render(request, 'tasks/index.html')    
