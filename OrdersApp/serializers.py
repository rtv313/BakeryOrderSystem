# -*- coding: utf-8 -*-
from OrdersApp.models import *
from rest_framework import serializers

    

class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields= ('id','Name','LastName','Phone','Status','Note','OrderDate')

      

    


class SearchOrder(serializers.Serializer):
    Status = serializers.CharField()
    
    