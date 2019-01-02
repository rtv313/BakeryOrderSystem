# -*- coding: utf-8 -*-
from OrdersApp.models import *
from rest_framework import serializers
from django.core.serializers import serialize

    

class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields= ('id','Name','LastName','Phone','Status','Note','OrderDate')
 
class SearchOrder(serializers.Serializer):
    Status = serializers.CharField()


class ProductApi(object):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price 

   
class ProductApiSerializer(serializers.Serializer): 
    name = serializers.CharField() 
    quantity = serializers.IntegerField()
    price = serializers.FloatField()


class ClientePedido():
    def __init__(self,Client,Products):
        self.Client = Client
        self.Products = Products


class ClientePedidoSerializer(serializers.Serializer):
    
    Client = ClientOrderSerializer()
    Products = ProductApiSerializer(many=True)
    
    def create(self,validated_data):
        return ClientePedido(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Name = validated_data.get("Client",instance.Client)
        instance.Products = validated_data.get("Products",instance.Products)
        return instance
    

class ProductResume():
    def __init__(self,ProductName,Quantity):
        self.ProductName = ProductName
        self.Quantity = Quantity

class ProductResumeSerializer(serializers.Serializer):
    ProductName = serializers.CharField() 
    Quantity = serializers.IntegerField()


class ProductDataResume():
    def __init__(self,ProductName,Quantity,Cost,Price):
        self.ProductName = ProductName
        self.Quantity = Quantity
        self.Cost = Cost
        self.Price = Price

class ProductDataResumeSerializer(serializers.Serializer):
    ProductName = serializers.CharField() 
    Quantity = serializers.IntegerField()
    Cost = serializers.FloatField()
    Price = serializers.FloatField()
     
class SalesReportData(serializers.Serializer):
    firstDate = serializers.DateField()
    secondDate = serializers.DateField()




    
    
    
    
    