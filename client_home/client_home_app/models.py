from django.db import models


class BaseClassForAudit(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ClientModel(BaseClassForAudit):
    """
    Model class for client info
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = 'client'

    def __str__(self):
        return self.name


class HouseModel(BaseClassForAudit):
    """
    Model class for Product info
    """
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    client_id = models.ForeignKey(ClientModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'house'

    def __str__(self):
        return '{}'.format(self.id)


class RoomModel(BaseClassForAudit):
    """
    Model class for Room info
    """
    id = models.AutoField(primary_key=True)
    room_type_and_count = models.CharField(max_length=50)
    house_id = models.ForeignKey(HouseModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'room'

    def __str__(self):
        return '{}'.format(self.house_id)


class ProductModel(BaseClassForAudit):
    """
    Model class for Product info
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    original_price = models.FloatField()
    discounted_price = models.FloatField()
    product_link = models.CharField(max_length=255)
    room_id = models.ForeignKey(RoomModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
