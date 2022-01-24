from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "accounts"
# urlpatterns = [
#   path('login/', auth_views.LoginView.as_view(), name='login'),
#   # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
# ]

# LoginView는 registration이라는 템플릿 디렉토리에서 login.html 파일을 찾는다.
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]