from django.contrib import admin
from OrdersApp.models import *
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    