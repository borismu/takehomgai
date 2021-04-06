from contextlib import suppress
from django.db import models
from django.utils.functional import cached_property


class StateContainer(models.Model):
    """
    Container that holds state

    Possible state transitions are:
    Stopped -> Started
    Started -> Waiting
    Waiting -> Executing
    Executing -> Waiting
    Waiting -> Stopping
    """

    STARTING = "STARTING"
    STARTED = "STARTED"
    WAITING = "WAITING"
    EXECUTING = "EXECUTING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"

    STATE_CHOICES = [
        (STARTING, STARTING),
        (STARTED, STARTED),
        (WAITING, WAITING),
        (EXECUTING, EXECUTING),
        (STOPPING, STOPPING),
        (STOPPED, STOPPED),
    ]

    STATE_POSSIBLE_CHANGES = {
        STOPPED: set([STARTED]),
        STARTED: set([WAITING]),
        WAITING: set([EXECUTING, STOPPING]),
        EXECUTING: set([WAITING]),
    }

    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=STARTING,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.pk} state: {self.state}"

    def change_state(self, new_state):
        if not self.is_next_state_eligible(new_state):
            raise Exception(
                f"Can't change state from {self.state} to {new_state}")
        self.state = new_state
        self.save()

    def is_next_state_eligible(self, new_state):
        with suppress(KeyError):
            return new_state in self.STATE_POSSIBLE_CHANGES[self.state]
        return False
