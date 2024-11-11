from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import articles, comments
import requests
from django.shortcuts import render

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
    
def weather(request):
    api_url = 'https://api.open-meteo.com/v1/forecast?latitude=54.6269&longitude=39.6916&current=temperature_2m,relative_humidity_2m,is_day,wind_speed_10m,wind_direction_10m&timezone=Europe%2FMoscow&forecast_days=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    return render(request, 'weather.html', {'data': data})
    
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
    
    