# CRUDTestProject
Django를 이용해 만든 간단한 부서관리 사이트. CRUD를 구현하는데 목적.

## 버전 정보
- DJango 4.0.1

## 개발 기간
2022.01.21 ~ 2022.01.26

## 기능
- 로그인
- admin User 등록
- 로그아웃
- 비밀번호 변경
- 유저 인증 예외처리
- 부서, 사원 목록 출력
- 부서, 사원 등록
- 부서, 사원 검색
- 부서, 사원 pagination

## 개발 과정 정리
### model 설계 
**부서 리스트(ListView) - 부서 정보(DetailView)**
- 부서번호 id(id) - Integer - PK
- 부서명 (dept)-  String
- 부서 설명(dept_explanation)- String
- 부서 위치(dept_position) - String

**사원 리스트(ListView) - 사원 정보(DetailView)**
- 사원번호id(id) -  Integer -PK
- 사원명(emp_name)- String
- 직급(emp_rank) - String
- 담당업무(emp_resposibilites) - String
- 월급여(monthly_salary) - Integer
- 입사일자(entry_date) - Date
- 부서번호(team_number)- FK

### base.html
매번 app안에서 base.html을 만드는 것은 번거롭고 틀을 두고 쓴다는 개념과는 너무 동떨어지는 거 같아서 방법을 찾아보았다.
- root 디렉토리에 templates 디렉토리 생성 후(앱 디렉토리와 같은 선상에 만들어 주면 된다)그 안에 base.html을 만들어 준다.<br>
![crud_1](https://user-images.githubusercontent.com/33194594/151470055-b37f9fbb-39e0-43e3-ac79-95c6fe47e90c.png)
<br>템플릿 확장에 쓸 base.html을 생성. base.html에서 계속 쓸 소스도 templates에 같이 넣어줄 수 있다. 예를 들어 head라든지.
내 경우는 부트스트랩을 불러오는 부분과 navbar를 추가했다.


```python
<!DOCTYPE html>
<html lang="en">
<head>
    {% include 'CND.html' %}
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% include 'navbar.html' %}

<div class="container my-3">
{% block main_block %}
{% endblock %}

</div>

</body>
</html>
```

다른 템플릿에서```{% extends 'base.html' %}```로 확장해서 쓸 수 있고 ```{% block main_block %}~{% endblock %}``` 안의 내용들이 base.html의 body 안에 보여지게 된다.

- 경로 잡아주기 <br>
프로젝트의 settings.py로가서 경로를 설정해 준다. ```‘DIRS’:[]```   대괄호 안에 ```os.path.join(BASE_DIR,'templates')```를 넣어준다.<br>
![crud_2](https://user-images.githubusercontent.com/33194594/151472400-a4e8a3cb-6afd-4cf4-b70e-7e71a2f80736.png)

BASE_DIR, 'templates'을 통해 기본 경로가 templates 라는 것을 설정. 앱에서 {% extends 'blog.html' %}을 통해서 확장을 시켜줄 수가 있다.

### FK 설정하기 
사원을 등록할때 이미 등록되어 있는 부서정보를 가져와서 등록하고 싶었다.
1. 다른 앱에 있는 모델을 import 한다. 
2. 부서 고유 번호를 받을 수 있도록 ForieignKey설정

emp/models.py
```python
from django.db import models
from django.contrib.auth.models import User
import uuid
from hrd.models import team #음 요렇게?? 다른 앱에 있는 모델 사용할 때

# Create your models here.

class employee(models.Model):
    emp_uuid = str(uuid.uuid4()) # 임의의 랜덤 문자열
    emp_name = models.CharField(max_length=30)
    team_number = models.ForeignKey(team, null=True, on_delete=models.SET_NULL) #다른 모델에 있는 부서 ForeignKey로 설정
    emp_rank = models.CharField(max_length=30)
   
```

![crud_3](https://user-images.githubusercontent.com/33194594/151477402-37a7d860-d5f1-4c44-b8eb-e19a98e239e1.png)

### 부서 상세페이지에 해당 사원 띄우기

앱을 2개를 만들어서 각각 모델을 생성했다. 부서 상세페이지에서 해당 부서에 해당하는 사원 리스트를 띄울 때 사원앱(emp)에 있는 모델을 쓸 필요가 있었다. 
1. views.py에 model import 
2. objects.filter를 이용에 조건에 맞는 데이터 조회
    이 부분에서 pk를 가져오는 부분을 몰라서 헤맴. kwargs를 이용해서 가져올 수 있었다

hrd/views.py
```python
from django.shortcuts import render
from .models import team
from emp.models import employee  # 해당 팀의 팀원들을 가지고 오고 싶어
from django.views.generic import ListView, DetailView


# Create your views here.
class TeamList(ListView):
    model = team
    ordering = '-pk'


class TeamDetail(DetailView):
    model = team

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data()
        context['team_member'] = employee.objects.filter(team_number=self.kwargs['pk']).values() #pk만 가져오는 방법
        return context

```

### DeleteView 없이 모달로 삭제
삭제하겠는지를 묻는 확인창을 모달로 띄워서 처리하고 싶었다. urls.py에 이름 지정부분으로 좀 헤맴.
1. views.py에 DeleteView 추가
2. urls.py에 path 추가 
3. 삭제 버튼이 위치하는 템플릿에 모달 추가. 모달안에 form을 넣어서 post로 넘겨줘야한다.
 
hrd/views.py
```python
# 삭제 ( 템플릿 없이 모달로만)
class TeamDelete(DeleteView):
    model = team
    success_url = reverse_lazy('team_li')  # urls.py에 이름을 지정해줘야(team_li) 적용이 되네 ㅠ  삭제후 띄울 화면
    template_name = 'hrd/team_list.html'
```
hrd/urls.py
```python
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
```
hrd/templates/hrd/team_detail.html
```python
 {# 유저인지 아닌지에 따라서 수정, 삭제 버튼 유무 설정 #}
    {% if user.is_authenticated %}
        {% if user.is_superuser or user.is_staff %}

            {# 삭제 버튼 눌렀을 때 모달띄우기#}
            <a class="btn btn-info btn-sm float-right m-2" href=" " role="button"
               data-toggle="modal" data-target="#deleteModal">
                <i class="fas fa-pen"></i>&nbsp;&nbsp;삭제</a>


            <a class="btn btn-info btn-sm float-right m-2" href="/hrd/team_update/{{ team.pk }}/" role="button">
                <i class="fas fa-pen"></i>&nbsp;&nbsp;수정</a>

            <a class="btn btn-info btn-sm float-left m-2" href="/hrd/" role="button">
                <i class="fas fa-align-justify"></i>&nbsp;&nbsp;목록</a>


        {% endif %}
    {% endif %}

    <!-- Modal -->
    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
         aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">확인</h5>
                    {# x 표시 버튼 #}
                    {#                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">#}
                    {#                        <span aria-hidden="true">&times;</span></button>#}
                </div>
                <div class="modal-body"> 해당 부서를 삭제하시겠습니까?</div>
                <div class="modal-footer">
                    {#모달 안에서 form을 이용해서 post로 전달 urls.py 에서 이름(name='team_d') 설정#}
                    <form action="{% url 'team_d' pk=team.pk %}" method="POST">
                        {% csrf_token %}
                        <button class="btn btn-primary">삭제하기</button>
                    </form>


                    <button type="button" class="btn btn-primary" data-dismiss="modal">취소하기</button>
                </div>
            </div>
        </div>
    </div>
```
