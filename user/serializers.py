from rest_framework import serializers
from user.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'member_type', 'membership_date', 'membership_expiry_date']