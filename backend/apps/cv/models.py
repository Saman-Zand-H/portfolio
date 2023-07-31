import os
from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


def image_validator(file):
    name, ext = os.path.splitext(file.name)
    valid_exts = [".svg", ".png", ".jpg", ".jpeg", ".ico"]
    if ext.lower() not in valid_exts:
        raise ValidationError("invalid image was uploaded.")


# this is gonna be a singletone model
class CV(models.Model):
    about = models.TextField()
    image = models.ImageField(upload_to="cv_images")
    location = models.CharField(max_length=50, default=_("Mashhad"))
    
    def save(self, *args, **kwargs):
        if CV.objects.count() == 0:
            return super().save(*args, **kwargs)
        raise ValidationError(_("CV object already exists."))


class Image(models.Model):
    image = models.ImageField(upload_to="projects", 
                              null=True, 
                              blank=True)
    alt = models.CharField(max_length=50, 
                           blank=True, 
                           null=True)
    uuid = models.UUIDField(auto_created=True, 
                            default=uuid4,
                            unique=True,
                            editable=False)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.alt if self.alt is not None else "no alt"
    

class Technology(models.Model):
    name = models.CharField(max_length=20)
    icon = models.FileField(upload_to="technologies",
                            blank=True,
                            null=True,
                            validators=[image_validator])
    timestamp = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True,
                          null=True)
    uuid = models.UUIDField(default=uuid4,
                            editable=False,
                            unique=True,
                            auto_created=True)
    
    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class ImageProjectRelation(models.Model):
    image = models.ForeignKey(Image, 
                              on_delete=models.CASCADE,
                              to_field="uuid")
    project = models.ForeignKey("Project",
                                on_delete=models.CASCADE)
    

class TechnologyProjectRelation(models.Model):
    technology = models.ForeignKey(Technology, 
                                   on_delete=models.CASCADE,
                                   to_field="uuid")
    project = models.ForeignKey("Project",
                                on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    explanations = models.TextField(blank=True, null=True)
    images = models.ManyToManyField(Image, through=ImageProjectRelation)
    slug = models.CharField(max_length=100, unique=True)
    technologies = models.ManyToManyField(Technology, 
                                          through=TechnologyProjectRelation)
    timestamp = models.DateTimeField(auto_now=True)
    started_at = models.DateField(default=timezone.now)
    ended_at = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.slug
    
    def clean(self):
        super().clean()
        # make the slug a slug :)
        "-".join(self.slug.split(" "))
    