from celery import shared_task
import time

from .models import StateContainer

@shared_task
def update_state(sc_id, new_state: str):
    # adding sleep so it's easier to debug
    time.sleep(2)
    state_container = StateContainer.objects.get(pk=sc_id)
    state_container.change_state(new_state)