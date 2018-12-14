# -*- coding: utf-8 -*-
from OrdersApp.models import *
from rest_framework import serializers

    

class ClientOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrder
        fields= ('Name','LastName','Phone','Status','Note','OrderDate')

      

    



    