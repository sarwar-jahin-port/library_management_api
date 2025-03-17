from django.shortcuts import render
<<<<<<< Updated upstream

# Create your views here.
=======
from rest_framework.viewsets import ModelViewSet
from user.models import Member
from user.serializers import UserCreateSerialier

# Create your views here.

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = UserCreateSerialier
>>>>>>> Stashed changes
