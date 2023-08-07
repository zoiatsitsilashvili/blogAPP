# from . import views

from django.urls import path,include
from . views import PostView, CategoryView, UserView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', PostView, 'post')
router.register(r'categories', CategoryView)
router.register(r'users', UserView )

urlpatterns = [
   path('', include(router.urls))
]


# urlpatterns = [
#     path('posts/', views.PostsAPIView.as_view(), name='posts'),
#     path('posts/<int:post_id>/', views.PostAPIView.as_view(), name='post'),
#     path('categories/', views.CategoryListAPIView.as_view(), name='categories'),
#     path('users/', views.UsersAPIView.as_view(), name='users'),
# ]
