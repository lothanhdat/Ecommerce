from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from base.serializers import UserSerializer, UserSerializerWithToken, OrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

from base.models import Product, Order, OrderItem, ShippingAddress
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']
    if orderItems and len(orderItems)==0:
        message = {'detail': 'No order items'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)
    else:
        #1. create order
        order = Order.objects.create(
            user = user,
            paymentMethod = data['paymentMethod'],
            taxPrice = data['taxPrice'],
            shippingPrice = data['shippingPrice'],
            totalPrice = data['totalPrice'],
        )

        #2. create shipping address
        shipping = ShippingAddress.objects.create(
            order = order,
            address = data['shippingAddress']['address'],
            city = data['shippingAddress']['city'],
            postalCode = data['shippingAddress']['postalCode'],
            country = data['shippingAddress']['country'],
        )

        #3. create order item
        for i in orderItems:
            product = Product.objects.get(_id=i['product'])
            item = OrderItem.objects.create(
                product = product,
                order = order,
                name= product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )

            product.countInStock -= item.qty
            product.save()
        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request,pk):
    user = request.user
    try:
        order = Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order,many=False)
            return Response(serializer.data)
        else:
            return Response({'detail':'not authorized to view this order'}, status=status.HTTP_400_BAD_REQUEST)
    except:
            return Response({'detail':'order does not exists'}, status=status.HTTP_400_BAD_REQUEST)