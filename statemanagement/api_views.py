from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import StateContainer
from .serializers import StateContainerSerializer, StateChangeSerializer
from .tasks import update_state


class StateContainerViewset(ModelViewSet):
    """
    Simple modelviewset to give ability easily manipulate data
    """
    queryset = StateContainer.objects.all()
    serializer_class = StateContainerSerializer


class StateChange(APIView):
    """
    Views for changing state
    """
    serializer_class = StateChangeSerializer

    # TODO convert to async def
    def post(self, request, format=None):
        serializer = StateChangeSerializer(data=request.data)
        # perform basic data validation
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        # pulling data from request
        sc_id = serializer.validated_data["id"]
        new_state = serializer.validated_data["new_state"]

        # validating object exists and new_state is correct
        if not serializer.validated_data["bypass_state_validation"]:
            sc = get_object_or_404(StateContainer, pk=sc_id)
            if not sc.is_next_state_eligible(new_state):
                return Response("New state is incorrect",
                                status=status.HTTP_400_BAD_REQUEST)

        # Task scheduling
        task = update_state.delay(sc_id, new_state)

        if not serializer.validated_data["wait_until_complete"]:
            return Response(f"Task {task.id} was scheduled",
                            status=status.HTTP_202_ACCEPTED)
        
        # TODO add asyncio waiting and checking
        return Response(f"Task {task.id} ended with {task.status}",
                        status=status.HTTP_200_OK)
