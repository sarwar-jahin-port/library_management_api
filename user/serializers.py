from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerialier(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'email', 'address', 'membership_date', 'membership_expiry_date', 'member_type']