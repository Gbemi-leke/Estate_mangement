from django.dispatch import receiver 
from django.db.models.signals import (
    post_save,
)
from django.contrib.auth.models import User
from frontend.models import UserProfile


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    # update user profile
    if created:
        UserProfile.objects.create(
            user=instance
        )