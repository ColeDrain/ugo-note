from django.db import models
from django.utils import timezone
from django.utils import timezone
from taggit.managers import TaggableManager
from django.conf import settings
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    """Model definition for Post."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    cover_text = models.TextField(null=True, blank=True)
    body = models.TextField()
    tags = TaggableManager()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    """Model definition for Comment."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        """Unicode representation of Comment."""
        return f'{self.author} commented on {self.post}'

