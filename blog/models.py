from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # def published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=7) <= self.published_date <= now

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name="comments")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.name} - {self.text}"