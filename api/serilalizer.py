from rest_framework import serializers
from api.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id",'name','price','discount','tax','status','quantity']