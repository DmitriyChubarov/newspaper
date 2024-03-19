from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class ArticlesListView(ListView):
    model = models.articles
    template_name = 'articles_list.html'

class ArticlesUpdateView(UpdateView):
    model = models.articles
    fields = ['title', 'body']
    template_name = 'articles_update.html'
    success_url = reverse_lazy('articles_list')

class ArticlesDeleteView(DeleteView):
    model = models.articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')


class ArticlesDetailView(DetailView):
    model = models.articles
    template_name = 'articles_detail.html'

class ArticlesCreateView(CreateView):
    model = models.articles
    template_name = 'articles_create.html'
    fields = ['author', 'title', 'body']
    success_url = reverse_lazy('articles_list')
