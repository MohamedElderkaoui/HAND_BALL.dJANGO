

from rest_framework import serializers
from .models import Player, PlayerStats

# Serializer for Player
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

# Serializer for PlayerStats
class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = '__all__'
