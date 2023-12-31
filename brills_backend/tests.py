from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile, Expense
from .serializers import UserProfileSerializer

class ExpenseAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_profile = UserProfile.objects.create(user=self.user, email='test@example.com', name='Test User')

        self.expense_data = {
            'user': self.user,
            'name': 'Test Expense',
            'description': 'This is a test expense.',
            'cost': '50.00',
        }
        self.expense = Expense.objects.create(**self.expense_data)

    def test_create_expense(self):
        new_username = 'testuser2'
        user = User.objects.create_user(username='new_uwername', password='testpass')
        user_serializer = UserProfileSerializer(user)
        serialized_user = user_serializer.data

        self.expense_data['user'] = serialized_user
        response = self.client.post('/api/expenses/', data=self.expense_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 1)  

    def test_read_expense(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_update_expense(self):
        updated_data = {'name': 'Updated Expense', 'cost': '75.00'}
        response = self.client.put(f'/api/expenses/{self.expense.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.expense.refresh_from_db()
        self.assertEqual(self.expense.name, 'Updated Expense')
        self.assertEqual(str(self.expense.cost), '75.00')

    def test_delete_expense(self):
        response = self.client.delete(f'/api/expenses/{self.expense.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Expense.objects.count(), 0)

# You can add more tests for error cases, edge cases, etc.