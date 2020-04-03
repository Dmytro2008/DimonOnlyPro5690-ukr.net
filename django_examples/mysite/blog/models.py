from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='')
    comment = models.TextField(default='')

    class Meta:
        ordering = ['title']
    def get_absolute_url(self):
        return reverse('index')
    #def __str__(self):
        #return self.title
