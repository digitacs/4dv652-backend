from django.urls import path
from . import views

app_name = 'scores'
urlpatterns = [
    path("v1/scores", views.Version1.as_view()),
    path("v2/scores", views.Version2.as_view())
]
