from rest_framework import serializers
from scores.models import Request
from scores.models import CamRequest


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class CamRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamRequest
        fields = '__all__'
