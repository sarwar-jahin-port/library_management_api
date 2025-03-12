from django.urls import path, include
from rest_framework_nested import routers
from book.views import BookViewSet, AuthorViewSet, CategoryViewSet
from user.views import MemberViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('members', MemberViewSet, basename='members')
router.register('author', AuthorViewSet, basename='author')
router.register('category', AuthorViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
