import os
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from mdeditor.fields import MDTextField


def image_validators(file):
    name, ext = os.path.splitext(file.name)
    valid_exts = [".png", ".jpg", ".jpeg"]
    if ext not in valid_exts:
        raise ValidationError("invalid image extension", 
                              "invalid_image")


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
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
    article = MDTextField()
    tags = models.ManyToManyField(Tag,
                                  blank=True,
                                  related_name="tag_articles")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slug
    
    def get_base_contents(self):
        if self.headings is None:
            return Heading.objects.none()
        return self.headings.filter(parent_heading__isnull=True)
    
    def parse_contents(self):
        """generates a parsed representation of the heading and subheadings in the format
        
        ' 
            {
                (heading_text, heading_id): {#here goes subheadings if they exists},
                
                ...
            }
        '

        Returns:
            Dict[tuple: Dict]: a representation of contents in a tree like dict
        """
        results = {}
        
        def dfs(content, ctx=results):
            print(f"{content} - {content.subheadings.exists()}")
            if not ctx.get(content, False):
                ctx[f"{content.heading_text},{content.heading_id}"] = {}
            if not content.subheadings.exists():
                return
            for heading in content.subheadings.all():
                ctx[f"{content.heading_text},{content.heading_id}"][f"{heading.heading_text},{heading.heading_id}"] = {}
                if heading.subheadings.exists():
                    dfs(content, ctx[f"{content.heading_text},{content.heading_id}"])
            return ctx
        
        for content in self.get_base_contents():
            dfs(content)
            
        return results
            
    
    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)
        
        
class Heading(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name="headings")
    heading_text = models.CharField(max_length=30)
    heading_id = models.CharField(max_length=30)
    parent_heading = models.ForeignKey("self",
                                       on_delete=models.CASCADE,
                                       related_name="subheadings",
                                       blank=True,
                                       null=True)
    
    def __str__(self):
        return f"{self.article.title} : {self.heading_text}"
