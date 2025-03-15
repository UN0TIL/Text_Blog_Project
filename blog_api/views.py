from rest_framework import generics, filters
from blog.models import Post
from .serializers import PostSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import CursorPagination
from .perimissions import IsAuthorOrReadOnly

# Create your views here.
class StandardResultsSetPagination(CursorPagination):
    page_size = 1
    page_size_query_param = 'cursor'
    orderering  = '-id'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['body', 'author__username']
    ordering_fields = ['author__id', 'publish']
    ordering = ['body']
    
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsAuthorOrReadOnly,)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = (IsAuthorOrReadOnly,)

class UserPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)
    
