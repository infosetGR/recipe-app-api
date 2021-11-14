from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with email success"""
        email = 'test@infoset.co'
        password='Test123'
        user= get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_lowcase(self):
        """Test user email gets normalized-lowercase"""
        email = 'test@INFOSET.co'
        password='Test123'
        user= get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email.lower())
        

    def test_new_user_invalid_email(self):
        """Test user email with invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"Test123")

    def test_create_new_superuser(self):
        """Test create superuser"""
        email = 'test@INFOSET.co'
        password='Test123'
        user= get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
        