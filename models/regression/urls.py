from django.urls import path
from models.regression import views

urlpatterns = [
    path("", views.PredictView.as_view(), name="predict")
]
