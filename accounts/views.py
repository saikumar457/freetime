from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.base import TemplateResponseMixin,View
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from . import forms
# Create your views here.

class NewUser(CreateView):
    template_name = "registration/sign_up_check.html"
    form_class = forms.NewUserForm
    success_url = reverse_lazy("connect:home")

    def form_valid(self,form):
        user = super().form_valid(form)
        cd = form.cleaned_data
        user_login=authenticate(self.request,username=cd["username"],password=cd["password1"])
        login(self.request,user=user_login)
        return user

def validate_user(request):
    username = request.GET.get("username",None)
    mail = request.GET.get("email",None)
    data = {
        "user_error":User.objects.filter(username__iexact=username).exists(),
        "mail_error":User.objects.filter(email__iexact=mail).exists()
    }

    if data["user_error"] or data["mail_error"]:
        data["user_warn"] = "User already existed"
        data["mail_warn"] = "Mail already existed"

    return JsonResponse(data)


class UserRegister(CreateView):
    template_name = "registration/sign_up.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("connect:home")

    def form_valid(self,form):
        user = super(UserRegister,self).form_valid(form)
        cd = form.cleaned_data
        user.set_password(cd["password1"])
        user_login = authenticate(username=cd["username"],password=cd["password1"])
        login(self.request,user_login)
        return user
