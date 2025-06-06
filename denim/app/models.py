from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Jacket', 'Jacket'),
        ('Jeans', 'Jeans')
    ])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name 
    
class ProductImage(models.Model):
    Product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return f"Image for {self.Product.name}"
    
class Banner(models.Model):
    image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return f"Banner {self.id}"