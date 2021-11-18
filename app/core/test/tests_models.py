from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='fotis@infoset.co', password = 'testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email,password)

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
        
    def test_tag_str(self):
        """Test tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name='Vegan'
            )
        
        self.assertEqual(str(tag),tag.name)
    
    def test_ingredient_str(self):
        """Test Ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user = sample_user(),
            name='salt'
            )
        
        self.assertEqual(str(ingredient),ingredient.name)



