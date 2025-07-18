from rest_framework.viewsets import ModelViewSet
from ..models import SubCategory
from ..serializers import SubCategorySerializer

class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
