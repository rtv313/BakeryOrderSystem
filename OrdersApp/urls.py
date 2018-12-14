from django.conf.urls import url
from OrdersApp import views,viewsRestFul

urlpatterns = [
    url(r'^ClientMenu/$', views.ClientMenu,name='ClientMenu'),
    url(r'^MakeOrder/$', views.MakeOrder,name='MakeOrder'),
    url(r'^Orders/$', viewsRestFul.Orders.as_view()),
    ]