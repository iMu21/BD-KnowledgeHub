from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from examination.models import topicNames

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_comment_likes")
    ordering = ['created_at']
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.ForeignKey(topicNames, on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name="post_comment")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    ordering = ['-post_date']

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args=(str(self.pk)))

