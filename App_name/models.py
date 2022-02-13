from django.db import models

# Create your models here.
# from django.contrib.auth.models import User

class BlogPost(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    description = models.TextField()


    def __str__(self):
        return self.name

