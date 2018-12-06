# -*- coding: utf-8 -*-
from OrdersApp.models import *
from rest_framework import serializers

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ('id','Name','LastName','Phone','Status','Note','OrderDate')
        

class ClientOrderSerializer(serializers.ModelSerializer):
    model = ClientOrder
    fields = ('Name','LastName','Phone','Status','Note','OrderDate')


class OrderProductSerializer(serializers.ModelSerializer):
    model = OrderProduct
    fields = ('Quantity','Client','Product')