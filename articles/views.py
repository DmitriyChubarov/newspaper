from django.shortcuts import render
from django.views.generic import ListView
from . import models

class ArticlesListView(ListView):
    model = models.articles
    template_name = 'articles_list.html'
