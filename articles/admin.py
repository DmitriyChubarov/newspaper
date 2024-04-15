from django.contrib import admin

from . import models

admin.site.register(models.articles)
admin.site.register(models.comments)
