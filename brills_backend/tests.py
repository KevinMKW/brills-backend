from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Profile

class ProfileTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile_data = {"data": {"name": "Test User", "email": "test@example.com", "income": "5000", "currency": "Zimbabwe Dollar (Z$)"}}


    def test_create_profile(self):
        response = self.client.post('/api/profile/', {"data": self.profile_data})
        print(response.data)
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_profile_list(self):
        response = self.client.get('/api/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_profile_detail(self):
        profile = Profile.objects.create(name="Test User", email="test@example.com")
        response = self.client.get(f'/api/profile/{profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test User')

    def test_update_profile(self):
        profile = Profile.objects.create(name='Old Name', email='old@example.com')
        updated_data = {"data": {"name": "New Name", "email": "new@example.com"}}
        response = self.client.put(f'/api/profile/{profile.id}/', updated_data)
        if response.status_code != status.HTTP_200_OK:
            print(response.data) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile(self):
        profile = Profile.objects.create(name='Test User', email='test@example.com')
        response = self.client.delete(f'/api/profile/{profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Profile.objects.count(), 0)

