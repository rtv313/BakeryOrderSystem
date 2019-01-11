from OrdersApp.models import *
from django.contrib.auth.models import User
from OrdersApp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse,HttpResponseForbidden
import datetime
from datetime import datetime,timedelta
from django.db.models import Sum
import base64

#token 89f39b9d21b410971637dc5a76d60ab85a3a8da8
class Orders(APIView):
    
    def put(self,request,format=None):
        
        searchData = SearchOrder(data=request.data)
        
        if not searchData.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
     
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
    
    
class OrderDetail(APIView):
    
    def get(self,request,pk,format=None):
        
        client  = ClientOrder.objects.get(pk=pk)   
        orders = OrderProduct.objects.filter(Client_id = client.pk)
        list = []
        
        for order in orders:
            product = ProductApi(name=order.Product.Name ,quantity= order.Quantity,price= order.Product.Price)
            list.append(product)
        
        
        cliente  = ClientePedido(client,list)
        answerRest = ClientePedidoSerializer(cliente)
        
        return Response(answerRest.data,status=status.HTTP_200_OK)
    
    def put (self,request,pk,format = None):
        
        searchData = SearchOrder(data=request.data)
        
        if not searchData.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
     
        selectedStatus = searchData.validated_data['Status'];
        
        client  = ClientOrder.objects.get(pk=pk) 
        client.Status = selectedStatus
        client.save()
        
        return Response(status=status.HTTP_200_OK)
    
class OrdersResume(APIView):
    
    def get (self,request,format = None):
        
        products = OrderProduct.objects.filter(Client__Status = "PENDIENTE").values('Product__Name').annotate(Sum('Quantity'))
        productResume = []
        
        for product in products: 
            name = product["Product__Name"]
            quantity = product["Quantity__sum"]
            productResume.append(ProductResume(name,quantity))
            
        answer = ProductResumeSerializer(productResume,many=True)
        
        return Response(answer.data,status=status.HTTP_200_OK)
    

class SalesReport(APIView):
    
    def post(self,request,format = None):
        
        datesData = SalesReportData(data=request.data)
        
        if not datesData.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        firstDate = datesData.validated_data['firstDate']
        secondDate = datesData.validated_data['secondDate']
        products = OrderProduct.objects.filter(Client__OrderDate__range = [firstDate,secondDate],Client__Status = "TERMINADO").values('Product__Name','Product__ProductionCost','Product__Price').annotate(Sum('Quantity'))
        productDataResume = []
        
        for product in products: 
            
            name = product["Product__Name"]
            quantity = product["Quantity__sum"]
            cost = product["Product__ProductionCost"]
            price = product["Product__Price"]
            
            productDataResume.append(ProductDataResume(name,quantity,cost,price))
            
        answer = ProductDataResumeSerializer(productDataResume,many=True)
        
        return Response(answer.data,status=status.HTTP_200_OK)
    

class Products(APIView):
    
    def get(self,request,format = None):
        
        products = Product.objects.all().order_by('-Name')
        answer = ProductSerializer(products,many = True)
        return Response(answer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format = None):
        
        newProductData = AddProductSerializer(data=request.data)
        
        if not newProductData.is_valid():
            return Response(newProductData.errors, status=status.HTTP_400_BAD_REQUEST)
        
        newProductData.save()
        
        return Response(newProductData.data,status=status.HTTP_200_OK)



        
        
        
        
    