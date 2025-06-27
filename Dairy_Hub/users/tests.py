from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            name="Jane Wambui",
            phone_number="0712345678",
            email="jane@gmail.com",
            password_hash="@123password",
            type="Supplier"
        )
        
        self.assertEqual(user.name, "Jane Wambui")
        self.assertEqual(user.phone_number, "0712345678")
        self.assertEqual(user.email, "jane@gmail.com")
        self.assertEqual(user.type, "Supplier")
        self.assertEqual(user.password_hash, "@123password")
        self.assertIn("Supplier", str(user))  