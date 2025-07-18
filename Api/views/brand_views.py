from rest_framework.viewsets import ModelViewSet
from ..models import Brand
from ..serializers import BrandSerializer

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'