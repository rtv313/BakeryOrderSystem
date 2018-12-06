from django.contrib import admin
from OrdersApp.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name','Price')
    search_fields = ['Name']
   
admin.site.register(Product,ProductAdmin)



class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ['productName']

    def productName(self,obj):
        return obj.Product.Name

class ClientOrderAdmin(admin.ModelAdmin):
    list_display = ('Name','LastName','Phone','Status','OrderDate')
    search_fields = ['Name','LastName']
    inlines = [ OrderProductInline, ]
    
admin.site.register(ClientOrder,ClientOrderAdmin)
    