from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255 ,unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
       

    def __str__(self):
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name = 'items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
   
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name