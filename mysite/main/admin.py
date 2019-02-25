from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "date", "slug"]}),
        ("Content", {"fields": ["body"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

# Register your models here.
admin.site.register(Article, ArticleAdmin)