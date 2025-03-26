from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Product
from api.serilalizer import ProductSerializer
from api.pagination import CustomPagination

# -------- Manage Products (Create, Update, List) --------

@api_view(['GET', 'POST', 'PUT'])
def manage_products(request):
    # ---------- GET ----------
    if request.method == 'GET':
        products = Product.objects.exclude(status=1)

        if not products.exists():
            return Response(
                {"message": "No products found"},
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------- POST ----------
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Product created successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message': 'Invalid data provided'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # ---------- PUT ----------
    elif request.method == 'PUT':
        product_id = request.data.get('id')
        if not product_id:
            return Response(
                {'message': 'Product ID is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {'message': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Product updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'Invalid data provided'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # ---------- Method Not Allowed ----------
    return Response(
        {'message': 'Method not allowed'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


# -------- Get Specific Product --------
@api_view(['POST'])
def get_product(request):
    product_id = request.data.get('id')
    if not product_id:
        return Response(
            {'message': 'Product ID is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(
            {'message': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

# -------- Get All Products --------
@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.exclude(status=1)

    if not products.exists():
        return Response({"message": "No products found"}, status=status.HTTP_204_NO_CONTENT)

    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

# -------- Delete Product (Soft Delete by status) --------
@api_view(['PUT'])
def delete_product(request):
    product_id = request.data.get('id')
    if not product_id:
        return Response(
            {'message': 'Product ID is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {'message': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    product.status = 1  # Soft delete
    product.save()

    return Response(
        {'message': 'Product deleted successfully'},
        status=status.HTTP_200_OK
    )