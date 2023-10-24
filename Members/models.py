from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfilManager(models.Manager):
    def create_profil(self, user):
        profil = self.create(user=user)
        return profil

class Profail(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="static/user_photo/",blank=True,default="static\img\images.png")
    address=models.CharField(max_length=200,default='user')
    phone_number = models.CharField(max_length=20,default='user')
    objects=ProfilManager()
    def __str__(self):
        return str(self.user)

