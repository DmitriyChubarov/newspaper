from django.urls import path, include
from .views import SignUp, LogOut, ChangePass
from users import views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout', views.LogOut.as_view(),  name='logout_'),
    path('password_change/', views.ChangePass.as_view(),  name='changepass'),
]