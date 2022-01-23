from django.urls import path
from . import views


urlpatterns = [
    path('', views.TeamList.as_view()),
    path('hrd/<int:pk>/', views.TeamDetail.as_view()),
    path('hrd/teamcreate/', views.TeamCreate.as_view()),
    path('hrd/team_update/<int:pk>/', views.TeamUpdate.as_view()), #update뷰는 꼭 pk를 넣어서 보내야
]