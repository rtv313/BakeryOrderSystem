# -*- coding: utf-8 -*-  
from django.shortcuts import render
from OrdersApp.models import *
from django.conf import settings
from django.shortcuts import redirect
from datetime import datetime 
import requests  
import urllib
import json
# Create your views here.



def ClientMenu (request):
    
    products = Product.objects.all();
    
    if request.method == 'GET':
        return render(request, 'OrdersApp/BreadMenu.html',{'products':products,'url_media':settings.MEDIA_DOMAIN })
    
    if request.method == 'POST':
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
    	
            breads = request.POST.getlist('breads')
            Name = request.POST.get("name", "")
            LastName = request.POST.get("lastname", "")
            Phone = request.POST.get("tel", "")
            Note = request.POST.get("note", "")
            OrderDate = datetime.now()
            clientOrder = ClientOrder.objects.create(Name=Name,LastName=LastName,Phone=Phone,Status="PENDIENTE",Note=Note,OrderDate=OrderDate)
            clientOrder.save()
            
            for bread in breads:
                productId = bread.split("-")[0]
                productQuantity = bread.split("-")[1]
                selectedBread = Product.objects.get(pk=productId)
                orderProduct = OrderProduct.objects.create(Quantity = productQuantity,Client= clientOrder,Product = selectedBread)
                orderProduct.save();
            
            
            headers = {'Content-Type': 'application/json','Authorization':settings.FIRE_BASE }
            requests.post('https://fcm.googleapis.com/fcm/send',
                          json = {'to':'/topics/NuevosPedidos'},
                          headers = headers)
            
            return redirect('MakeOrder')
        else:
            return redirect('MakeOrder')
   
    return render(request, 'OrdersApp/BreadMenu.html',{'products':products,'url_media':settings.MEDIA_DOMAIN })

def MakeOrder (request):
    
    return render(request,'OrdersApp/OrderMenu.html',{})




