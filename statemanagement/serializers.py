from rest_framework import serializers

from .models import StateContainer


class StateContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateContainer
        read_only_fields = ('id', 'created', 'modified')
        fields = read_only_fields + ('state',)
