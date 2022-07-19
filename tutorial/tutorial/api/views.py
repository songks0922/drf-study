from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from api.models import Book
from api.serializers import BookSerializer


class ListBookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title', 'description', 'sell_count']