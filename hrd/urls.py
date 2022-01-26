from django.urls import path
from . import views


urlpatterns = [
    path('', views.TeamList.as_view(), name='team_li'), #모달로 삭제하는 부분하면서 name 설정
    path('hrd/<int:pk>/', views.TeamDetail.as_view()),
    path('hrd/teamcreate/', views.TeamCreate.as_view()),
    path('hrd/team_update/<int:pk>/', views.TeamUpdate.as_view()), #update뷰는 꼭 pk를 넣어서 보내야
    path('<int:pk>/team_delete', views.TeamDelete.as_view(), name ='team_d'), #모달로 삭제하는 부분하면서 name 설정
    path('hrd/search/<str:q>/', views.TeamSearch.as_view()),#검색
]