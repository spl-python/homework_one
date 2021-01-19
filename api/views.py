from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter

from api.filter import ComputerFilterSet
from api.models import Computer
from api.pagination import MyPageNumberPagenation, MyCursorPagination, MyLimitOffsetPagination
from api.serializer import ComputerModelSerializer
from api.throttle import MyThrottle


class UserAPIView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response('OK')

    def post(self, request, *args, **kwargs):
        return Response('写操作')


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
    # filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]

    filter_backends = [DjangoFilterBackend]
    # search_fields = ['name','price']

    ordering = ['price']

    filter_class = ComputerFilterSet

    pagination_class = MyPageNumberPagenation
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
