from django.shortcuts import render
from .models import team
from emp.models import employee  # 해당 팀의 팀원들을 가지고 오고 싶어
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# CreateView 하면서 추가 된 부분
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.shortcuts import render, redirect

# Update하면서 추가 된 부분
from django.core.exceptions import PermissionDenied


# Create your views here.
class TeamList(ListView):
    model = team
    ordering = '-pk'


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
