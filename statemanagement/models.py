from django.db import models


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

    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default=STARTING,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {self.pk} state: {self.state}"
