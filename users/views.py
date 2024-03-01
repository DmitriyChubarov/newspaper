from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LogOut(TemplateView):
    template_name = 'logout.html'

class ChangePass(TemplateView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('home')