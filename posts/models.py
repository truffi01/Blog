from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length = 100)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete =models.CASCADE)

    class Meta:
        verbose_name_plural = "posts"
    
    def __str__(self):
        return f'{self.post_title}'