from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reciepes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    reciepe_name = models.CharField(max_length=50)
    reciepe_desc = models.TextField()
    reciepe_img = models.ImageField(upload_to="reciepe_images")


    def __str__(self)-> str:
        return self.reciepe_name



