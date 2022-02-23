from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def post_save_user(created, instance, **kwargs):
    if created:
        print(f"Poljzovatelj {instance.username} sohranjon!!!!!!")
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



