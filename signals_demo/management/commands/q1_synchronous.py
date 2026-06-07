import time
from django.core.management.base import BaseCommand
from signals_demo.models import MyModel

class Command(BaseCommand):
    help = 'Q1: Proves Django signals are synchronous'

    def handle(self, *args, **kwargs):
        print("[Caller] About to save MyModel instance...")
        start = time.time()
        MyModel.objects.create(name="test_sync")
        end = time.time()
        elapsed = end - start
        print(f"[Caller] Save returned. Total time elapsed: {elapsed:.2f}s")
        print("[Caller] If elapsed >= 3s, the caller WAITED for the signal = synchronous.")
