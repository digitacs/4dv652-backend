from rest_framework import generics
from django.http import HttpResponse

from models.regression.models import LRRequest


def home(request):
    return HttpResponse('<p>view</p>')

# class LRRequestList(generics.ListCreateAPIView):
    # pass
