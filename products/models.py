from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('shoes', 'Shoes'),
        ('wears', 'Wears'),
        ('accessories', 'Accessories'),
        ('skincare', 'Skincare'),
    ]

def validate_image_size(value):
    # 1MB = 1024 * 1024 bytes
    max_size = 1024 * 1024
    if value.size > max_size:
        raise ValidationError(f"The image size should not exceed {max_size} bytes (1MB).")
    

class Product(models.Model):
    Name = models.CharField(max_length= 105)
    Description = models.TextField(blank=True, null=True)  # Optional field
    Price = models.DecimalField(max_digits= 10, decimal_places=2)
    Quantity = models.IntegerField(default= 0)
    Category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='electronics')
    Image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Image field
    Created_At = models.DateTimeField(auto_now_add=True)  # Timestamp for product creation
    Updated_At = models.DateTimeField(auto_now=True)  # Updates timestamp on every save

    def __str__(self): #it format the display name on the admin panel 
        return self.Name
    
    #dunder str method