from django.db import models
from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFill
# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=100,unique=True)
    Price = models.FloatField()
    ProductionCost = models.FloatField()
    Image = ProcessedImageField(upload_to='ProductImages/',
                                           processors=[ResizeToFill(700,400)],
                                           format='PNG',
                                           options={'quality': 95})

ORDER_STATUS = (("PENDIENTE","PENDIENTE"),("TERMINADO","TERMINADO"),("CANCELADO","CANCELADO"),("ENTREGADO","ENTREGADO"))

class ClientOrder(models.Model):
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Phone =  models.CharField(max_length=30)
    Status = models.CharField(max_length=11,choices=ORDER_STATUS,default="PENDIENTE")
    Note  = models.TextField(blank=True)
    OrderDate = models.DateTimeField()
    
class OrderProduct(models.Model):
    Quantity = models.IntegerField()
    Client = models.ForeignKey(ClientOrder,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
   

