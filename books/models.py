from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,blank=True)
    published_year = models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)