from rest_framework import serializers
from .models import StaticInfo


class StaticInfoSerializer(serializers.ModelSerializer):

    #static_info = serializers.StringRelatedField(many=True)

    class Meta:
        model = StaticInfo
        fields = (
            'static_info_id',
            'value',
            'combo_type',
            'is_active',
        )

