'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers

from .models import User, UserStatus


class UserProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(many=True)

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
            'user',
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

