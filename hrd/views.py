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
