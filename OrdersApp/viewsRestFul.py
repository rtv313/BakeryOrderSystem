from OrdersApp.models import *
from django.contrib.auth.models import User
from OrdersApp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse,HttpResponseForbidden
import datetime
from datetime import datetime,timedelta


#token 89f39b9d21b410971637dc5a76d60ab85a3a8da8
class Orders(APIView):
    
    def put(self,request,format=None):
        
        searchData = SearchOrder(data=request.data)
        
        if not searchData.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        print(searchData.validated_data['Status'])
        
        selectedStatus = searchData.validated_data['Status'];
        
        clients = None
        actualDate = datetime.now().date() + timedelta(days=1)
        threeWeeksBefore = datetime.now().date() - timedelta(days=14)
        
        if selectedStatus == "PENDIENTE":
            clients = ClientOrder.objects.filter(Status="PENDIENTE").order_by('-id')
        
        if selectedStatus == "TERMINADO": 
            clients = ClientOrder.objects.filter(Status="TERMINADO",OrderDate__range=[threeWeeksBefore,actualDate]).order_by('-id')
        
        if selectedStatus == "CANCELADO": 
            clients = ClientOrder.objects.filter(Status="CANCELADO",OrderDate__range=[threeWeeksBefore,actualDate]).order_by('-id')
        
            
        clientSerializer  = ClientOrderSerializer(clients,many=True)
        return Response(clientSerializer.data, status=status.HTTP_200_OK)
    