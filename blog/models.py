from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    author = models.CharField(null=False, blank=False, max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.title
