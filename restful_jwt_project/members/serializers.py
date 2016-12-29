from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from common.constants import *

from rest_framework.serializers import ModelSerializer


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "email", "name", "phone", "reg_date", "last_mod_date", ]

