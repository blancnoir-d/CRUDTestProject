"""crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#미디어 파일을 위한 URL 처리 (이걸 제대로 해줘야 admin에서 이미지를 누를때 원본이 보인다)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hrd.urls')),
    path('hrd/',include('hrd.urls')),
    path('emp/',include('emp.urls')),
]


#미디어 파일을 위한 URL 처리
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)