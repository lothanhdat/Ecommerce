from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from base.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from base.models import Product


# Create your views here.

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product=Product.objects.get(_id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user = user,
        name = 'sample name',
        price = 100,
        brand = 'sample brand',
        countInStock = 100,
        category = 'sample category',
        description = ''
    )
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    product=Product.objects.get(_id=pk)
    data = request.data
    product.name = data['name']
    product.price = data['price']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']
    product.name = data['name']
    product.save()

    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)