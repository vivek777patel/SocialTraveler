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
            'description',
            'photo_link',
            'created_date',
            'updated_date',
            'location_det_info',
            'is_active',
            'review',
        )
        model = LocationDetails

