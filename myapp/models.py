from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    marks=models.IntegerField()
    subject=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    def __str__(self):
        return self.name
    
class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.title