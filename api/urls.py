from django.urls import path, include
from rest_framework_nested import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
