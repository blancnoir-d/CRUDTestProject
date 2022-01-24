from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmpList.as_view(), name = 'emp_li'),
    path('<int:pk>/', views.EmpDetail.as_view()), #emp/숫자
    path('create_emp/', views.EmpCreate.as_view()),
    path('update_emp/<int:pk>/', views.EmpUpdate.as_view()),
    path('<int:pk>/delete_emp', views.EmpDelete.as_view(),name='emp_d')
]