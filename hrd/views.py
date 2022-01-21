from django.shortcuts import render
from .models import team
from django.views.generic import ListView, DetailView


# Create your views here.
class TeamList(ListView):
    model = team
    ordering = '-pk'


class TeamDerail(DetailView):
    model = team
