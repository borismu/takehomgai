from rest_framework import serializers

from .models import StateContainer


class StateContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateContainer
        read_only_fields = ('id', 'created', 'modified')
        fields = read_only_fields + ('state',)


class StateChangeSerializer(serializers.Serializer):
    wait_until_complete = serializers.BooleanField()
    bypass_state_validation = serializers.BooleanField()
    new_state = serializers.CharField()
    id = serializers.CharField()