from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .serializers import LocationInfoSerializer
from .models import LocationInfo



# @api_view(["POST"])
# @authentication_classes((TokenAuthentication,))
# @permission_classes((IsAuthenticated,))
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#
#     user = authenticate(email=username, password=password)
#
#     if not user :
#         return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
#
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key})



# For /location/addLocationInfo/ --> Kind of URL
# Post Request


class AddLocationInfo(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = LocationInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /location/1/ --> Kind of URL
# Get Request
# For /location/allLocationInfoList/ --> Kind of URL
# Post Request


class LocationInfoDetail(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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
