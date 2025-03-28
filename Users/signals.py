from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import profile, CustomUser

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
