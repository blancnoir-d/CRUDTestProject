from django.urls import path
from . import views


urlpatterns = [
    path('', views.TeamList.as_view()),
    path('hrd/<int:pk>/', views.TeamDetail.as_view())
]