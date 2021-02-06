# Create your views here.

from rest_framework import generics

from scores.models import Score
from scores.serializers import ScoreSerializer


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

