from rest_framework.pagination import PageNumberPagination, CursorPagination

class ProductPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductCursorPagination(CursorPagination):
    page_size = 4
    ordering = 'product_id'