from django.urls import path
from . import views


urlpatterns = [
    path('', views.TeamList.as_view()),
]