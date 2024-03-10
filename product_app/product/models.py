from django.db import models

# Create your models here.
class Product(models.Model):
    # eid=models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    price = models.FloatField()
    category = models.CharField(max_length=90)
    vendor = models.CharField(max_length=80)  
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    class Meta:
        db_table="Product_Master"
    

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)