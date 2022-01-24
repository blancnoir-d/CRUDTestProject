from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import employee

# CreateView 하면서 추가 된 부분
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect


# Create your views here.

class EmpList(ListView):
    model = employee


class EmpDetail(DetailView):
    model = employee


class EmpCreate(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = employee
    fields = ['emp_name', 'team_number', 'emp_rank', 'emp_responsibilities', 'monthly_salary', 'entry_date', 'image']

    def CheckUser(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(EmpCreate, self).form_valid(form)
            return response
        else:
            return redirect('/emp/')


class EmpUpdate(UpdateView, LoginRequiredMixin):
    model = employee
    fields = ['emp_name', 'team_number', 'emp_rank', 'emp_responsibilities', 'monthly_salary', 'entry_date', 'image']

    def get_context_data(self, **kwargs):
        context = super(EmpUpdate, self).get_context_data()
        return context

    def form_valid(self, form):
        response = super(EmpUpdate, self).form_valid(form)
        return response
