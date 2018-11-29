from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk':self.pk})


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.ImageField()

