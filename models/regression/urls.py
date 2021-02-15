from django.urls import path
from models.regression import views

urlpatterns = [
    #path("", views.LRRequestList.as_view()),
    path("", views.home)
]
