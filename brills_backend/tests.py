from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile, Bill
from .serializers import UserProfileSerializer

class BillAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(user=self.user, email='test@example.com', name='Test User')

        self.Bill_data = {
            'user': self.user,
            'name': 'Test Bill',
            'description': 'This is a test Bill.',
            'cost': '50.00',
        }
        self.Bill = Bill.objects.create(**self.Bill_data)

    def test_create_Bill(self):
        new_username = 'testuser2'
        user = User.objects.create_user(username='new_uwername', password='testpass')
        user_serializer = UserProfileSerializer(user)
        serialized_user = user_serializer.data

        self.Bill_data['user'] = serialized_user
        response = self.client.post('/api/Bills/', data=self.Bill_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bill.objects.count(), 1)  

    def test_read_Bill(self):
        response = self.client.get('/api/Bills/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_update_Bill(self):
        updated_data = {'name': 'Updated Bill', 'cost': '75.00'}
        response = self.client.put(f'/api/Bills/{self.Bill.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.Bill.refresh_from_db()
        self.assertEqual(self.Bill.name, 'Updated Bill')
        self.assertEqual(str(self.Bill.cost), '75.00')

    def test_delete_Bill(self):
        response = self.client.delete(f'/api/Bills/{self.Bill.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bill.objects.count(), 0)

# You can add more tests for error cases, edge cases, etc.