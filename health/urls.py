from django.urls import path
from health import views

urlpatterns = [
    path("", views.home, name="home"),
]