from celery import shared_task

from .models import StateContainer

@shared_task
def update_state(sc_id, new_state: str):
    state_container = StateContainer.objects.get(pk=sc_id)
    state_container.change_state(new_state)