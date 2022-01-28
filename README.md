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

## 과정 정리
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
- root 디렉토리에 templates 디렉토리 생성 후(앱 디렉토리와 같은 선상에 만들어 주면 된다)그 안에 base.html을 만들어 준다.
![crud_1](https://user-images.githubusercontent.com/33194594/151470055-b37f9fbb-39e0-43e3-ac79-95c6fe47e90c.png)
<br>템플릿 확장에 쓸 base.html을 생성. base.html에서 계속 쓸 소스도 templates에 같이 넣어줄 수 있다. 예를 들어 head라든지. <br>
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
프로젝트의 settings.py로가서 경로를 설정해 준다. ‘DIRS’:[]   대괄호 안에 os.path.join(BASE_DIR,'templates')를 넣어준다
![crud_2](https://user-images.githubusercontent.com/33194594/151472400-a4e8a3cb-6afd-4cf4-b70e-7e71a2f80736.png)

