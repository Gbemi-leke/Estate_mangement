from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileTest(TestCase):
    def test_user_model_has_profile(self):
        user = User(
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        tel = self.cleaned_data['tel']
        user_image = self.cleaned_data['user_image']
        )
        user.save()

        self.assertTrue(
            hasattr(user, 'profile')
        )