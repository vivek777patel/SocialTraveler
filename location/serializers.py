'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers

from .models import LocationInfo


class LocationInfoSerializer(serializers.ModelSerializer):

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
        )
        model = LocationInfo

