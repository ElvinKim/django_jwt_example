from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from members.models import Member
from members.serializers import MemberListSerializer
from members.serializers import MemberDetailSerializer


class MemberListAPIView(ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer


class MemberDetailAPIView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer


