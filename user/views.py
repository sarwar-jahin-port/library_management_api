from rest_framework.viewsets import ModelViewSet
from user.models import Member
from user.serializers import UserCreateSerialier
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# Create your views here.

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = UserCreateSerialier
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]