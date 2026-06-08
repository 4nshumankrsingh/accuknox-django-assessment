import threading
from django.core.management.base import BaseCommand
from signals_demo.models import MyModel

class Command(BaseCommand):
    help = 'Q2: Proves Django signals run in the same thread as the caller'

    def handle(self, *args, **kwargs):
        print(f"[Caller] Thread ID: {threading.current_thread().ident}")
        MyModel.objects.create(name="test_thread")
