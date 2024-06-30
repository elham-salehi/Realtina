from rest_framework import serializers

from .models import List, Reservation


# Serializer for List model
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


# Serializer for Reservation model
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
