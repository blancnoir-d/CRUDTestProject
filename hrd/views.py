from django.shortcuts import render

from .models import team
from emp.models import employee  # 해당 팀의 팀원들을 가지고 오고 싶어
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# CreateView 하면서 추가 된 부분
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.shortcuts import render, redirect

# Update하면서 추가 된 부분
from django.core.exceptions import PermissionDenied

# Delete 하면서 추가 된 부분
from django.urls import reverse_lazy

# 검색구현하면서 추가된 부분
from django.db.models import Q


# Create your views here.
class TeamList(ListView):
    model = team
    ordering = ['-pk']
    paginate_by = 3


class TeamDetail(DetailView):
    model = team

    def get_context_data(self, **kwargs):
        context = super(TeamDetail, self).get_context_data()
        context['team_member'] = employee.objects.filter(team_number=self.kwargs['pk']).values()  # pk만 가져오는 방법
        return context


# 등록 - CreateView를 쓰면 html에 모델_form.html이 있어야함.
class TeamCreate(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = team
    fields = ['team_name', 'team_position', 'team_explanation']

    def CheckUser(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(TeamCreate, self).form_valid(form)
            return response
        else:
            return redirect('/hrd/')


# 수정
class TeamUpdate(UpdateView, LoginRequiredMixin):
    model = team
    fields = ['team_name', 'team_position', 'team_explanation']

    template_name = 'hrd/team_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(TeamUpdate, self).get_context_data()
        return context

    # 본래 dispatch는 get, post 방식인지 확인하는 함수. 여기서는 접근 권한이 있는 방문자인지 확인하는 용도로 활용
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and request.user == self.get_object().author:
    #         return super(TeamUpdate, self).dispatch(request, *args, **kwargs)
    #     else:
    #         raise PermissionDenied

    def form_valid(self, form):
        response = super(TeamUpdate, self).form_valid(form)
        return response


# 삭제 ( 템플릿 없이 모달로만)
class TeamDelete(DeleteView):
    model = team
    success_url = reverse_lazy('team_li')  # urls.py에 이름을 지정해줘야(team_li) 적용이 되네 ㅠ  삭제후 띄울 화면
    template_name = 'hrd/team_list.html'


# 검색기능
class TeamSearch(TeamList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        #Q : 여러 조건을 사용하고 싶을 때 사용
        team_list = team.objects.filter(
            Q(team_name__contains=q)
        ).distinct() #중복 제거
        return team_list

    def get_context_data(self, **kwargs):
        context = super(TeamSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context
