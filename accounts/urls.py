from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
# urlpatterns = [
#   path('login/', auth_views.LoginView.as_view(), name='login'),
#   # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
# ]

# LoginView는 registration이라는 템플릿 디렉토리에서 login.html 파일을 찾는다.
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('register/', views.UserCreate.as_view(), name='regi'),
  path('register_done/', views.RegisterDone.as_view(), name='register_done'),
  # path('pass_change/', views.PasswordChange.as_view(), name='pass_change'),
  path('pass_change/', views.change_password, name='pass_change'),
  path('pass_change_done/', views.PasswordChangeDone.as_view(), name='pass_change_done'),
  path('logout/', views.LogoutView.as_view(template_name='accounts/log_out.html'), name='logout'),
]
