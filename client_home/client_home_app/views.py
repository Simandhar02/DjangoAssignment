from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from client_home.settings import logger

from .models import ClientModel, ProductModel, HouseModel, RoomModel
from .serializers import ProductModelSerializer, HouseModelSerializer, RoomModelSerializer, ClientModelSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def client_view(request, client_id):
    try:
        client = check_client(client_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The client does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        client_serializer = ClientModelSerializer(client)
        return JsonResponse(client_serializer.data)

    elif request.method == 'PUT':
        # client_data = JSONParser().parse(request)
        # client_serializer = ClientModelSerializer(client, data=client_data)
        # if client_serializer.is_valid():
        #     client_serializer.save()
        #     return JsonResponse(client_serializer.data)
        # return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return put_request_update_data(request, client, ClientModelSerializer)

    elif request.method == 'DELETE':
        logger.info("Deleting data for Client")
        client.delete()
        return JsonResponse({'message': 'Client was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_client(request):
    if request.method == 'POST':
        return post_request_add_data(request, ClientModelSerializer)
        # client_data = JSONParser().parse(request)
        # client_serializer = ClientModelSerializer(data=client_data)
        # if client_serializer.is_valid():
        #     client_serializer.save()
        #     return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        return post_request_add_data(request, ProductModelSerializer)
        # product_data = JSONParser().parse(request)
        # product_serializer = ProductModelSerializer(data=product_data)
        # if product_serializer.is_valid():
        #     product_serializer.save()
        #     return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_view(request, pk):
#     try:
#         product = check_product(product_id)
#     except ProductModel.DoesNotExist:
#         return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)
# 
#     if request.method == 'GET':
#         product_serializer = ProductModelSerializer(product)
#         return JsonResponse(product_serializer.data)
# 
#     elif request.method == 'PUT':
#         # product_data = JSONParser().parse(request)
#         # product_serializer = ProductModelSerializer(product, data=product_data)
#         # if product_serializer.is_valid():
#         #     product_serializer.save()
#         #     return JsonResponse(product_serializer.data)
#         # return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return put_request_update_data(request, product, ProductModelSerializer)
# 
#     elif request.method == 'DELETE':
#         product.delete()
#         return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_house(request):
    if request.method == 'POST':
        return post_request_add_data(request, HouseModelSerializer)
        # house_data = JSONParser().parse(request)
        # house_serializer = HouseModelSerializer(data=house_data)
        # if house_serializer.is_valid():
        #     house_serializer.save()
        #     return JsonResponse(house_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def house_view(request, house_id):
    try:
        house = check_house(house_id)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        house_serializer = HouseModelSerializer(house)
        return JsonResponse(house_serializer.data)

    elif request.method == 'PUT':
        # house_data = JSONParser().parse(request)
        # house_serializer = HouseModelSerializer(house, data=house_data)
        # if house_serializer.is_valid():
        #     house_serializer.save()
        #     return JsonResponse(house_serializer.data)
        # return JsonResponse(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return put_request_update_data(request, house, HouseModelSerializer)

    elif request.method == 'DELETE':
        logger.info("Deleting data for House")
        house.delete()
        return JsonResponse({'message': 'House was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_house_for_client(request, client_id):
    if request.method == 'GET':
        try:
            client = check_client(client_id)
            house = HouseModel.objects.all().filter(client_id=client_id)
            house_serializer = HouseModelSerializer(house, many=True)
            return JsonResponse(house_serializer.data, safe=False)
        except ClientModel.DoesNotExist:
            return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT', 'DELETE', 'GET'])
def client_house_modify(request, client_id, house_id):
    try:
        client = check_client(client_id)
        house = check_house(house_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        house = HouseModel.objects.all().filter(client_id=client_id,
                                                pk=house_id)
        house_serializer = HouseModelSerializer(house, many=True)
        return JsonResponse(house_serializer.data, safe=False)

    elif request.method == 'PUT':
        # house_data = JSONParser().parse(request)
        # house_serializer = HouseModelSerializer(house, data=house_data)
        # if house_serializer.is_valid():
        #     house_serializer.save()
        #     return JsonResponse(house_serializer.data)
        # return JsonResponse(house_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return put_request_update_data(request, house, HouseModelSerializer)

    elif request.method == 'DELETE':
        house.delete()
        return JsonResponse({'message': 'House was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_rooms_for_client_house(request, client_id, house_id):
    try:
        client = check_client(client_id)
        house = check_house(house_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The Client does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        room = RoomModel.objects.all().filter(house_id=house_id)
        room_serializer = RoomModelSerializer(room, many=True)
        return JsonResponse(room_serializer.data, safe=False)


@api_view(['POST'])
def add_room(request):
    if request.method == 'POST':
        return post_request_add_data(request, RoomModelSerializer)
        # room_data = JSONParser().parse(request)
        # room_serializer = RoomModelSerializer(data=room_data)
        # if room_serializer.is_valid():
        #     room_serializer.save()
        #     return JsonResponse(room_serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
def modify_clients_rooms(request, client_id, house_id, room_id):
    try:
        client = check_client(client_id)
        house = check_house(house_id)
        room = check_room(room_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The Client {} does not exist'.format(client_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House {} does not exist'.format(house_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except RoomModel.DoesNotExist:
        return JsonResponse({'message': 'The Room {} does not exist'.format(room_id)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        room = RoomModel.objects.all().filter(pk=room_id,
                                              house_id=house_id)
        room_serializer = RoomModelSerializer(room, many=True)
        return JsonResponse(room_serializer.data, safe=False)

    elif request.method == 'PUT':
        # room_data = JSONParser().parse(request)
        # room_serializer = RoomModelSerializer(room, data=room_data)
        # if room_serializer.is_valid():
        #     room_serializer.save()
        #     return JsonResponse(room_serializer.data)
        # return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return put_request_update_data(request, room, RoomModelSerializer)

    elif request.method == 'DELETE':
        logger.info("Deleting data for Room")
        room.delete()
        return JsonResponse({'message': 'Room was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_products_for_room(request, client_id, house_id, room_id):
    try:
        client = check_client(client_id)
        house = check_house(house_id)
        room = check_room(room_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The Client {} does not exist'.format(client_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House {} does not exist'.format(house_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except RoomModel.DoesNotExist:
        return JsonResponse({'message': 'The Room {} does not exist'.format(room_id)}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        product = ProductModel.objects.all().filter(room_id=room_id)
        product_serializer = ProductModelSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)


@api_view(['PUT', 'DELETE', 'GET'])
def modify_products(request, client_id, house_id, room_id, product_id):
    try:
        client = check_client(client_id)
        house = check_house(house_id)
        room = check_room(room_id)
        product = check_product(product_id)
    except ClientModel.DoesNotExist:
        return JsonResponse({'message': 'The Client {} does not exist'.format(client_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except HouseModel.DoesNotExist:
        return JsonResponse({'message': 'The House {} does not exist'.format(house_id)},
                            status=status.HTTP_404_NOT_FOUND)
    except RoomModel.DoesNotExist:
        return JsonResponse({'message': 'The Room {} does not exist'.format(room_id)}, status=status.HTTP_404_NOT_FOUND)
    except ProductModel.DoesNotExist:
        return JsonResponse({'message': 'The Product {} does not exist'.format(product_id)},
                            status=status.HTTP_404_NOT_FOUND)
    # client, house, room, product = get_basic_data(client_id=client_id, house_id=house_id,
    #                                               room_id=room_id, product_id=product_id)

    if request.method == 'GET':
        product = ProductModel.objects.all().filter(pk=product_id,
                                                    room_id=room_id)
        product_serializer = ProductModelSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)

    elif request.method == 'PUT':
        # product_data = JSONParser().parse(request)
        # product_serializer = ProductModelSerializer(product, data=product_data)
        # if product_serializer.is_valid():
        #     product_serializer.save()
        #     return JsonResponse(product_serializer.data)
        # return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return put_request_update_data(request, product, ProductModelSerializer)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


def put_request_update_data(request, data, Serializer):
    logger.info("Updating data for {}".format(Serializer))
    product_data = JSONParser().parse(request)
    data_serializer = Serializer(data, data=product_data)
    if data_serializer.is_valid():
        data_serializer.save()
        return Response(data_serializer.data)
    return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def post_request_add_data(request, Serializer):
    logger.info("Adding data to {}".format(Serializer))
    data = JSONParser().parse(request)
    data_serializer = Serializer(data=data)
    if data_serializer.is_valid():
        data_serializer.save()
        return Response(data_serializer.data, status=status.HTTP_201_CREATED)
    return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def check_client(client_id):
    return ClientModel.objects.get(pk=client_id)


def check_product(product_id):
    return ProductModel.objects.get(pk=product_id)


def check_room(room_id):
    return RoomModel.objects.get(pk=room_id)


def check_house(house_id):
    return HouseModel.objects.get(pk=house_id)
