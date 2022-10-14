from rest_framework import serializers

from .models import Stuff


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ['name', 'service', 'created_at', 'updated_at']