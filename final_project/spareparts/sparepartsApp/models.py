from django.db import models
from django.utils import timezone
#A model is a description of a physical database table.(a model is a table and a table is a relation)

# Create your models here.
#defining category of engine
class Category(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False )
    def __str__(self):
        return self.name
#defining category for product
class Product(models.Model):
#referencing the category of the product
    Category_name = models.ForeignKey(Category,on_delete=models.CASCADE,null=False, blank=False)
    #reserved for date of arrival fields
    item_name = models.CharField(max_length=50, null = False, blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False,blank=False)
    received_quantity = models.IntegerField(default=0, null=False,blank=False)
    unit_price =models.IntegerField(default=0, null=False,blank=False) 


    def __str__(self):
        return self.item_name 