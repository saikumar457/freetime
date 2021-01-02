from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("sign_up/",views.UserRegister.as_view(),name="sign_up"),
    path("sign_up_check/",views.NewUser.as_view(),name="sign_up_check"),
    path("validate_user/",views.validate_user,name="validate_user"),
    path("login/",auth_views.LoginView.as_view(),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("password_change/",auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password_change_done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password_reset/",auth_views.PasswordResetView.as_view(),name="password_reset"),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64><token>/confirm/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
