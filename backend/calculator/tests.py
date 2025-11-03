from django.test import TestCase
from rest_framework.test import APIClient

class CalculatorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_addition(self):
        data = {'num1': 5, 'num2': 3, 'operation': '+'}
        response = self.client.post('/api/calculate/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 8)

    def test_subtraction(self):
        data = {'num1': 5, 'num2': 3, 'operation': '-'}
        response = self.client.post('/api/calculate/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['result'], 2)
