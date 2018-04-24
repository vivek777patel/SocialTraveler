from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from .models import User, UserStatus, UserFriends
from .serializers import UserProfileSerializer, UserStatusSerializer, UserFriendsSerializer


# Create your views here.


@api_view(["POST"])
# @authentication_classes((TokenAuthentication,))
# @permission_classes((IsAuthenticated,))
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(email=username, password=password)

    if not user :
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    user_profile_serializer = UserProfileSerializer(user)
    return Response(user_profile_serializer.data)


# For /UserProfile/userDetails/1/ --> Kind of URL
# Post Request


class UserProfileDetail(APIView):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        user_profiles = User.objects.filter(is_active=1)
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk, is_active=1)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_profile = self.get_object(pk)
        user_profile_serializer = UserProfileSerializer(user_profile)
        return Response(user_profile_serializer.data)

    def put(self, request, pk):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For /UserProfile/addUserProfile/ --> Kind of URL
# Post Request


class AddUserProfile(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk, is_active=1)
        except User.DoesNotExist:
            raise Http404

    def post(self, request):

        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        user = User.objects.create_user(email=email, password=password)
        # Add other variables like below
        user.first_name = first_name
        user.save()
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


# For /userProfile/userStatus/addUserStatus/ --> Kind of URL
# Post Request


class AddUserStatus(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /userProfile/userFriends/addUserStatus/ --> Kind of URL
# Post Request


class AddUserFriends(APIView):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserFriendsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For /userProfile/userFriends/1/ --> Kind of URL
# Get Request


class UserFriendsDetail(APIView):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return UserFriends.objects.get(pk=pk, is_active=1)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user_friends = self.get_object(pk)
        user_friends_serializer = UserFriendsSerializer(user_friends)
        return Response(user_friends_serializer.data)

    def put(self, request, pk):
        user_friend = self.get_object(pk)
        serializer = UserFriendsSerializer(user_friend, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_friends = self.get_object(pk)
        user_friends.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# For /userProfile/userStatus/allUserStatus/ --> Kind of URL
# Post Request


class UserStatusList(APIView):
    '''
        If the below post method changed to get it will become get request (just change the keyword post-->get)
    '''

    def post(self, request):
        user_status = UserStatus.objects.filter(is_active=1)
        serializer = UserStatusSerializer(user_status, many=True)
        return Response(serializer.data)

