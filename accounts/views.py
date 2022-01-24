
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#비밀번호 변경
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

#로그아웃
from django.contrib.auth.views import LogoutView



# Create your views here.

# 유저 등록
class UserCreate(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:register_done')


class RegisterDone(TemplateView):
    template_name = 'accounts/register_done.html'


# class PasswordChange(CreateView):
#     template_name = 'accounts/password_change_form.html'
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('accounts:pass_change_done')
#     def get_context_data(self, **kwargs):


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:pass_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change_form.html', {
        'form': form
    })


class PasswordChangeDone(TemplateView):
    template_name = 'accounts/password_change_done.html'


class UserLogout(LogoutView):
    template_name = 'accounts/templates/registeration/log_out.html'
