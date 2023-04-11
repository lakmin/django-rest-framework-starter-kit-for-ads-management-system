from rest_framework import serializers
from .models import Deal
class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ["name", "completed","website","image", "description", "updated", "user"]
