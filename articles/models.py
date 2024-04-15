from django.db import models
from django.conf import settings
from django.urls import reverse

class articles(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('articles_detail', kwargs={'pk': self.id})


class comments(models.Model):
    article=models.ForeignKey(articles, on_delete=models.CASCADE,
                              related_name='comments')
    comment=models.CharField(max_length=255)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

def __str__(self):
    return self.comment

def get_absolute_url(self):
    return reverse('articles_list', kwargs={'pk': self.id})