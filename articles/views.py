from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import articles, comments
from django.shortcuts import get_object_or_404, render

class ArticlesListView(ListView):
    model = articles
    template_name = 'articles_list.html'

class ArticlesUpdateView(UpdateView):
    model = articles
    fields = ['title', 'body']
    template_name = 'articles_update.html'
    success_url = reverse_lazy('articles_list')

class ArticlesDeleteView(DeleteView):
    model = articles
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')


class ArticlesDetailView(DetailView):
    model = articles
    template_name = 'articles_detail.html'

class ArticlesCreateView(CreateView):
    model = articles
    template_name = 'articles_create.html'
    fields = ['author', 'title', 'body']
    success_url = reverse_lazy('articles_list')

class CommentsCreateView(CreateView):
    model = comments
    template_name = 'comments_create.html'
    fields = ['author', 'comment', 'article']
    success_url = reverse_lazy('articles_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_data'] = articles.objects.all()
        article_id = self.kwargs.get('pk', None)  
        if article_id:
            context['article_id'] = article_id  
        return context
    
    