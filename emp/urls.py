from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmpList.as_view()),
    path('<int:pk>/', views.EmpDetail.as_view()), #emp/숫자
    path('create_emp/', views.EmpCreate.as_view()),
    path('update_emp/<int:pk>/', views.EmpUpdate.as_view()),
]