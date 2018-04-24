from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LocationInfo
from .serializers import LocationInfoSerializer, VisitedLocationSerializer, LocationDetailsSerializer


class GetLocationInfoDetail(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_object(self, location_name):
        try:
            return LocationInfo.objects.get(location_name=location_name, is_active=1)
        except LocationInfo.DoesNotExist:
            raise Http404

    def get(self, request, location_name):
        location_info = self.get_object(location_name)
        location_info_serializer = LocationInfoSerializer(location_info)
        return Response(location_info_serializer.data)


# For /location/addLocationInfo/ --> Kind of URL
# Post Request


class AddLocationInfo(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = LocationInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /location/addVisitedLocationInfo/ --> Kind of URL
# Post Request


class AddVisitedLocationInfo(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = VisitedLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /location/addLocationDetail/ --> Kind of URL
# Post Request


class AddLocationDetails(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = LocationDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /location/1/ --> Kind of URL
# Get Request
# For /location/allLocationInfoList/ --> Kind of URL
# Post Request


class LocationInfoDetail(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        location_info = LocationInfo.objects.filter(is_active=1)
        serializer = LocationInfoSerializer(location_info, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return LocationInfo.objects.get(pk=pk, is_active=1)
        except LocationInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        location_info = self.get_object(pk)
        location_info_serializer = LocationInfoSerializer(location_info)
        return Response(location_info_serializer.data)

    def put(self, request, pk):
        location_info = self.get_object(pk)
        serializer = LocationInfoSerializer(location_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        location_info = self.get_object(pk)
        location_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
