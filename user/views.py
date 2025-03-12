from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.models import Member
from user.serializers import MemberSerializer

# Create your views here.

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer