from django.contrib import admin

from .models import (
    CV,
    Image,
    Technology,
    Project,
    ImageProjectRelation,
    TechnologyProjectRelation,
)


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    ...


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ...


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    ...


class InlineImage(admin.TabularInline):
    model = ImageProjectRelation


class InlineTechnology(admin.TabularInline):
    model = TechnologyProjectRelation


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [InlineImage, InlineTechnology]
