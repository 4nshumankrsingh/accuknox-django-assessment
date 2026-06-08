from django.core.management.base import BaseCommand
from django.db import transaction
from signals_demo.models import MyModel

class Command(BaseCommand):
    help = 'Q3: Proves Django signals run in the same database transaction as the caller'

    def handle(self, *args, **kwargs):
        print(f"[Caller] Records before test: {MyModel.objects.count()}")
        try:
            with transaction.atomic():
                MyModel.objects.create(name="test_transaction")
                print(f"[Caller] Record created inside transaction. Count now: {MyModel.objects.count()}")
                raise Exception("Intentional rollback!")
        except Exception as e:
            print(f"[Caller] Exception caught: {e}")

        print(f"[Caller] Records after rollback: {MyModel.objects.count()}")
        print("[Caller] If count is same as before, the signal's DB work was also rolled back = same transaction.")
