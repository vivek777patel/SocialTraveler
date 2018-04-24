'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers

from .models import LocationInfo, VisitedLocationInfo, LocationDetails


class LocationInfoSerializer(serializers.ModelSerializer):

    location_info = serializers.StringRelatedField(many=True)
    location_det_info = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'location_name',
            'address_line1',
            'address_line2',
            'address_line3',
            'city',
            'state',
            'country',
            'zip_code',
            'latitude',
            'longitude',
            'updated_time',
            'is_active',
            'location_info',
            'location_det_info',
            'review',
            'location_type',
        )
        model = LocationInfo


class VisitedLocationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'updated_time',
            'user_id',
            'location_id',
            'is_active',
        )
        model = VisitedLocationInfo


class LocationDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'photo_link',
            'media_type_static_info',
            'created_date',
            'updated_date',
            'location_det_info',
            'is_active',
        )
        model = LocationDetails

