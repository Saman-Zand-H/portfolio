from django.contrib import admin

from .models import Article, Tag, Heading


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    ...
