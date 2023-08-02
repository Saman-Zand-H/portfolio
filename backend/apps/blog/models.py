import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField


def image_validators(file):
    name, ext = os.path.splitext(file.name)
    valid_exts = [".png", ".jpg", ".jpeg"]
    if ext not in valid_exts:
        raise ValidationError("invalid image extension", 
                              "invalid_image")


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def save(self, *args, **kwargs):
        # avoiding dupication with different casings
        self.name = self.name.lower()
        return super().save(*args, **kwargs)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="user_articles")
    thumbnail = models.ImageField(upload_to="blog/thumbnails")
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, default="")
    slug = models.SlugField(unique=True, max_length=100)
    article = RichTextField()
    tags = models.ForeignKey(Tag,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             related_name="tag_articles")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)
    