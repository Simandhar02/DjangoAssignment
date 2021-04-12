from rest_framework import serializers

from .models import (ClientModel, HouseModel, ProductModel, RoomModel)


class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class HouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = '__all__'


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = '__all__'
