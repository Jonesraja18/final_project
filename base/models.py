from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.category_name
    
Status_choices=[
    ('draft','Draft'),
    ('published','Published')
]
class Articles(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=1000)
    short_description=models.TextField(max_length=10000)
    detail_description=models.TextField(max_length=100000)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='media')
    status=models.CharField(choices=Status_choices)
    is_treanding=models.BooleanField(default=False)
    

