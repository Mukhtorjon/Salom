
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Post(models.Model):
    CHOICES = (
        ('Qora', 'Qoralama'),
        ('Tay', 'Tayyor'),
    )   
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length= 50)
    title=models.CharField( max_length=100)
    body=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='static/img',blank=True)
    publik_time=models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=300, choices = CHOICES)
    blog_views=models.IntegerField(default=0)
    like=models.ManyToManyField(User,related_name='blog_posts')
    def incrementViewCount(self):
        self.blog_views += 1
        self.save()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse("blog-single", args=(str( self.id)))
        return reverse('index')
    
class Friendes(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/friendimage',blank=True)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    message=models.TextField(max_length=300)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    mail= models.EmailField(max_length = 254)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text