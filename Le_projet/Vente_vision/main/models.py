from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):#the test (deletable)
    name=models.CharField(max_length=100)
    des=models.TextField()
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title + '\n' + self.description