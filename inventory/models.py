from django.db import models

# Create your models here.

class Stock(models.Model):
    #name of columns
    category = models.CharField(max_length=200, blank=False) 
    product = models.CharField(max_length=50, default=" ")
    quantity = models.IntegerField()

    choices = (
        ('READY TO DISTRIBUTE', 'Item ready to be distributed'),
        ('DISTRIBUTED', 'Item already distributed'),
        ('NEEDS RESTOCKING', 'Item needs restocking')
    )

    status = models.CharField(max_length=50, choices=choices, default=' ')
    
    #to skip creation of table Stock because it is an abstract class
    class Meta:
        abstract = True

class Kitchenware(Stock):
    pass

class Chicken(Stock):
    pass