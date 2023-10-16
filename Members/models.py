from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profail(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="static/user_photo/",blank=True,null=True)
    address=models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
 
    def __str__(self):
        return str(self.user.username)