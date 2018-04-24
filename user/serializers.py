'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers

from .models import User, UserStatus, UserFriends


class UserProfileSerializer(serializers.ModelSerializer):

    user_status = serializers.StringRelatedField(many=True)
    visited_location_user = serializers.StringRelatedField(many=True)
    user1 = serializers.StringRelatedField(many=True)
    user2 = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'date_of_birth',
            'mobile',
            'gender',
            'last_login_time',
            'last_visited_location',
            'favourite_place',
            'current_profile_pic',
            'location_id',
            'is_active',
            'user_status',
            'visited_location_user',
            'user1',
            'user2',
        )
        model = User


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'status',
            'updated_time',
            'is_active',
            'user_id',
        )
        model = UserStatus


class UserFriendsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'user_friends_id',
            'user_id1',
            'user_id2',
            'are_friends_with',
            'updated_time',
        )
        model = UserFriends

