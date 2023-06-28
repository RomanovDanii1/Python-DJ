from rest_framework import generics

from .models import *
from .serializers import *


class PetList(generics.ListAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()

        category = self.request.query_params.get('Category')
        if category is not None:
            queryset = queryset.filter(PetCategory=Category)
        return queryset


class PetDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EditProfileList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditProfileSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        payment = self.request.query_params.get('Payment')
        if payment is not None:
            queryset = queryset.filter(UserPayment=Payment)
        return queryset


class PaymentList(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemList(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()





