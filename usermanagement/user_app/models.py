from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=25,blank=True, null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)    
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
  


