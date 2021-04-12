from django.urls import path

from .views import client_view, add_client, add_product, get_house_for_client, add_house, house_view, \
    client_house_modify, get_rooms_for_client_house, \
    add_room, modify_clients_rooms, get_products_for_room, modify_products

urlpatterns = [
    path('api/clients', add_client),
    path('api/clients/<client_id>', client_view),
    path('api/products', add_product),
    path('api/house', add_house),
    path('api/house/<house_id>', house_view),
    path('api/clients/<client_id>/houses', get_house_for_client),
    path('api/clients/<client_id>/houses/<house_id>', client_house_modify),
    path('api/rooms', add_room),
    path('api/clients/<client_id>/houses/<house_id>/rooms', get_rooms_for_client_house),
    path('api/clients/<client_id>/houses/<house_id>/rooms/<room_id>', modify_clients_rooms),
    path('api/clients/<client_id>/houses/<house_id>/rooms/<room_id>/products', get_products_for_room),
    path('api/clients/<client_id>/houses/<house_id>/rooms/<room_id>/products/<product_id>', modify_products)
]
