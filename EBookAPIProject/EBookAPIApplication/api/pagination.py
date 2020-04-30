from rest_framework.pagination import PageNumberPagination


class SmallSetPaginaton(PageNumberPagination):
    page_size = 3