from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blog_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_user')
    title = models.CharField(max_length= 200)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete= models.CASCADE, related_name= 'comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment