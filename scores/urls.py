from django.urls import re_path
from . import views

app_name = 'scores'
urlpatterns = [
    re_path(r'v1/scores/?$', views.Version1.as_view()),
    re_path(r'v2/scores/?$', views.Version2.as_view())
]
