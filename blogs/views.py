# from rest_framework.views import APIView
from rest_framework import viewsets
from django_filters import filterset
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category, User
from . serializers import PostSerializer, CategorySerializer, UserSerializer
from . pagination import PostsPagination, UsersPagination, CategoriesPagination
from . filters import PostFilter,UserFilter, CategoryFilter


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostsPagination
    filterset_class = PostFilter


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoriesPagination
    filterset_class = CategoryFilter


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UsersPagination
    filterset_class = UserFilter



# class PostsAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

# class PostAPIView(APIView):
#     def get(self, request, post_id):
#         try:
#             post = Post.objects.get(pk=post_id)
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

# class CategoryListAPIView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

# class UsersAPIView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

