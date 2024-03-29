from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, blank = False)
    
    def __str__(self):
        return self.name
    