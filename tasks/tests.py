from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Test Description'}
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        url = reverse('task-list')
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
    
    def test_get_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
    
    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
    
    def test_complete_task(self):
        url = reverse('task-complete', args=[self.task.id])
        response = self.client.patch(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'Completed')
