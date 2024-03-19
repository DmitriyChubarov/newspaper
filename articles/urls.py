from django.urls import path, include
from articles import views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    path('<int:pk>/update/', views.ArticlesUpdateView.as_view(), name='articles_update'),
    path('<int:pk>/delete/', views.ArticlesDeleteView.as_view(), name='articles_delete'),
    path('<int:pk>/', views.ArticlesDetailView.as_view(), name='articles_detail'),
    path('new/', views.ArticlesCreateView.as_view(), name='articles_create'),
]