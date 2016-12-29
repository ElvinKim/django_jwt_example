from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from common.constants import *

from rest_framework.serializers import ModelSerializer


class MemberListSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ["email", "name", "phone", "reg_date", "last_mod_date", ]


class MemberDetailSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "email", "name", "phone", "reg_date", "last_mod_date", ]
