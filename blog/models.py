from django.db import models
from django.utils import timezone
from django.conf import settings
# Canonical URL
from django.urls import reverse

# Para mostrar post publicados y no draft
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    # many to one
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        related_name= 'blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
# Para mostrar post publicados y no draft
    
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish'] #descendente
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    
    #canonical url
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[self.id]
        )