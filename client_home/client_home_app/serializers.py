from django.core.exceptions import FieldDoesNotExist
from rest_framework import serializers

from .models import (ClientModel, HouseModel, ProductModel, RoomModel)


class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
        # fields = ('id', 'name', 'email', 'phone', 'address', 'city', 'created_on', 'is_deleted')


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class HouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = '__all__'
        # fields = ('id', 'address', 'room_type', 'room_count'
        #           'created_on', 'modified_on', 'is_deleted')


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = '__all__'
        # fields = ('id', 'name', 'created_on', 'modified_on', 'is_deleted')
