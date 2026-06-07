import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def slow_signal_receiver(sender, instance, **kwargs):
    print("[Signal] Receiver started...")
    time.sleep(3)
    print("[Signal] Receiver finished after 3 seconds.")
