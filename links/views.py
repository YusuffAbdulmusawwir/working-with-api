from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from .models import Link
from links.serializers import LinkSerializer
# Create your views here.
class PostListApi(ListAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer
    queryset= Link.objects.all()

class PostCreateApi(CreateAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer


class PostDetailApi(RetrieveAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer
    queryset= Link.objects.all()

class PostUpdateApi(UpdateAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer


class PostDeleteApi(DestroyAPIView):
    quaryset=Link.objects.filter(active=True)
    serializer_class=LinkSerializer