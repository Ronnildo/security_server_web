from django.db import models

# Create your models here.
class Base(models.Model):
    created = models.DateField(name='created', auto_now_add=True)
    modified = models.DateTimeField(name='modified', auto_now=True)
    actived = models.BooleanField(name="actived", default=True)

    class Meta:
        abstract = True
class User(Base):   
    name = models.CharField(name='name', max_length=150)
    email = models.EmailField(name='e-mail', max_length=200, unique=True)
    password = models.CharField(name='password', max_length=200)

    def __str__(self):
        return self.name

class Data(Base):
    title = models.CharField(name='title', max_length=100)
    file = models.FileField(name='file', upload_to='data/')

    def __str__(self):
        return self.title.name