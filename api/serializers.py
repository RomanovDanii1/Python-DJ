from rest_framework import serializers
from .models import *


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditProfileForm
        fields = ('__all__')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')


class  OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('__all__')
