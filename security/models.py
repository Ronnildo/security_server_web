from django.db import models

# Create your models here.
class User(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=200)

