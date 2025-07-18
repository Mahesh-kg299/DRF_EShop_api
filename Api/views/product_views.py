from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Product
from ..serializers import ProductSerializer
from ..paginations import ProductPageNumberPagination, ProductCursorPagination

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('product_id')
    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination

    @action(detail=True, methods=['post'])
    def mark_out_of_stock(self, request, pk=None):
        product = self.get_object()
        if not product.in_stock:
            return Response({'flag': False})
        product.in_stock = False
        product.save()
        return Response({'flag': True})
        
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        products = Product.objects.filter(in_stock=True)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get("category")
        products = Product.objects.filter(category=category)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def delete_all(self, request):
        self.get_queryset().delete()
        return Response({'detail', 'all products record deleted.'})