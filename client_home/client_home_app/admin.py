from django.contrib import admin
from django.apps import apps
from .models import ClientModel, RoomModel, ProductModel, HouseModel
models = apps.get_models()


class ClientDetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'city', 'created_on', 'modified_on')
    search_fields = ('name', 'id', 'email')
    readonly_fields = list_display


class RoomDetails(admin.ModelAdmin):
    list_display = ('id', 'room_type_and_count', 'house_id', 'created_on', 'modified_on')
    readonly_fields = list_display
    search_fields = ('id', 'house_id')


class ProductDetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'original_price', 'discounted_price',
                    'product_link', 'room_id', 'created_on', 'modified_on')
    search_fields = ('id', 'name', 'room_id')
    readonly_fields = list_display


class HouseDetails(admin.ModelAdmin):
    list_display = ('id', 'address', 'client_id', 'created_on', 'modified_on')
    search_fields = ('id', 'client_id')
    readonly_fields = list_display


admin.site.register(ClientModel, ClientDetails)
admin.site.register(RoomModel, RoomDetails)
admin.site.register(ProductModel, ProductDetails)
admin.site.register(HouseModel, HouseDetails)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.site_header = 'Client Admin'
