from django.db import models

# Create your models here.


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100000000)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=50, default='mylogo.png')
