from django.urls import path
from scores import views

urlpatterns = [
    #path("", views.ScoreList.as_view()),
    path("", views.PredictView.as_view())
]
