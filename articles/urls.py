from django.urls import path, include
from articles import views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list')
]