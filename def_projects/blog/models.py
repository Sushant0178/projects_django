
from django.db import models

class Blogg(models.Model):
    blogger_title = models.CharField(max_length=200, default='No Title')
    blogger_name = models.CharField(max_length=100, default='Anonymous' )
    text = models.TextField(default='No Content')

    def __str__(self):
        return self.blogger_title


class Comment(models.Model):
    blog = models.ForeignKey(Blogg,related_name='comments',on_delete=models.CASCADE )
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Comment by {self.author} on {self.blog.blogger_name}s blog {self.blog.blogge_title}'
