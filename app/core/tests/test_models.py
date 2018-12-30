from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """check user can be created"""
        email = "test@flowmo.co"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        email = "test@FLOWMO.co"
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email_error(self):
        """check that an error is raised when no email is supplied when creating a user"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')


    def test_create_new_superuser(self):
        """test that a new superuser can be created"""
        user = get_user_model().objects.create_superuser(
            'test@flowmo.co',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
