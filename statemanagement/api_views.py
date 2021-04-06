from rest_framework import viewsets

from .models import StateContainer
from .serializers import StateContainerSerializer

class StateContainerViewset(viewsets.ModelViewSet):
    """
    Simple modelviewset to give ability easily manipulate data
    """
    queryset = StateContainer.objects.all()
    serializer_class = StateContainerSerializer