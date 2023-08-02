from django.contrib import admin

from .models import Article, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...