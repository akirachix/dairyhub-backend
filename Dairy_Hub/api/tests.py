
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            "name": "Joy Bright",
            "phone_number": "0712345678",
            "email": "joybright@gmail.com",
            "password_hash": "@password123",
            "type": "farmer"
        }
        self.user = User.objects.create(**self.user_data)
        self.url = "/api/users/"

    def test_create_user(self):
        new_data = {
            "name": "Mercy Mwikali",
            "phone_number": "0722123456",
            "email": "mercymwikali@gmail.com",
            "password_hash": "pass@1162",
            "type": "Supplier"
        }
        response = self.client.post(self.url, new_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        response = self.client.get(f"{self.url}{self.user.user_id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        updated_data = self.user_data.copy()
        updated_data["name"] = "Peter"
        response = self.client.put(f"{self.url}{self.user.user_id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Peter")

    def test_delete_user(self):
        response = self.client.delete(f"{self.url}{self.user.user_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

