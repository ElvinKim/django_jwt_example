from django.shortcuts import render
from rest_framework.generics import ListAPIView

from members.models import Member
from members.serializers import MemberSerializer


class MemberListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


