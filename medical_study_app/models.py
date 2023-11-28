from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField("Email: ", max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])
    
class Notegroup(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_private = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('notegroup-detail', args=[str(self.id)])
    
class Notecard(models.Model):
    
    title = models.CharField(max_length=200)
    definition = models.TextField(blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default = None)
    notegroup = models.ManyToManyField(Notegroup, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
       return reverse('notecard-detail', args=[str(self.id)])
    
