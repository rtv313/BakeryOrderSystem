from OrdersApp.models import *
from django.contrib.auth.models import User
from OrdersApp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse,HttpResponseForbidden

#token 89f39b9d21b410971637dc5a76d60ab85a3a8da8
class Orders(APIView):
    
    def get(self,request,format=None):
        
        clients = ClientOrder.objects.all()
        clientSerializer  = ClientOrderSerializer(clients,many=True)
        return Response(clientSerializer.data, status=status.HTTP_200_OK)
    