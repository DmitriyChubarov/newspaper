
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from articles.views import weather  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('articles/', include('articles.urls')),
    path('weather/', weather, name='weather'),
]
