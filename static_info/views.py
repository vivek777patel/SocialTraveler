from django.shortcuts import render

# Create your views here.

from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import StaticInfo
from .serializers import StaticInfoSerializer

class StaticInfoDisp(APIView):
    '''
        If the below post method changed to get it will become get request (just change the keyword post-->get)
    '''
    def post(self, request, format=None):
        static_info = StaticInfo.objects.filter(is_active=1)
        serializer = StaticInfoSerializer(static_info, many=True)
        return Response(serializer.data)

class AddStatusInfo(APIView):

    def post(self, request, format=None):
        serializer = StaticInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaticInfoDetail(APIView):

    def get_object(self, pk):
        try:
            return StaticInfo.objects.get(pk=pk,is_active=1)
        except StaticInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        StaticInfo = self.get_object(pk)
        StaticInfo = StaticInfoSerializer(StaticInfo)
        return Response(StaticInfo.data)

    def put(self, request, pk, format=None):
        StaticInfo = self.get_object(pk)
        serializer = StaticInfoSerializer(StaticInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        StaticInfo = self.get_object(pk)
        StaticInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)