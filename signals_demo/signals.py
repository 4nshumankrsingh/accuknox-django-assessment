import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def slow_signal_receiver(sender, instance, **kwargs):
    print("[Signal] Receiver started...")
    time.sleep(3)
    print("[Signal] Receiver finished after 3 seconds.")

@receiver(post_save, sender=MyModel)
def thread_check_receiver(sender, instance, **kwargs):
    print(f"[Signal] Thread ID: {threading.current_thread().ident}")

@receiver(post_save, sender=MyModel)
def transaction_check_receiver(sender, instance, **kwargs):
    count = MyModel.objects.count()
    print(f"[Signal] Inside signal receiver. DB count visible from signal: {count}")
