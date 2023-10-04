from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    
    def __str__(self):
        return f"Cliente: {self.name} - Descripción: {self.description}"