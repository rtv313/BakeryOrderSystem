from django.conf.urls import url
from OrdersApp import views,viewsRestFul

urlpatterns = [
    url(r'^ClientMenu/$', views.ClientMenu,name='ClientMenu'),
    url(r'^MakeOrder/$', views.MakeOrder,name='MakeOrder'),
    url(r'^Orders/$', viewsRestFul.Orders.as_view()),
    url(r'^OrderDetail/(?P<pk>[0-9]+)$', viewsRestFul.OrderDetail.as_view()),
    url(r'^OrdersResume/$',viewsRestFul.OrdersResume.as_view()),
    ]