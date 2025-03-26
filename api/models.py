from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField()
    tax = models.FloatField(null=True,blank=True)
    status =models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

