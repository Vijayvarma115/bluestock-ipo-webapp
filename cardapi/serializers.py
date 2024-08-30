from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Card
        fields = '__all__'
