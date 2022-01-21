from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import employee
# Create your views here.

class EmpList(ListView):
    model = employee
