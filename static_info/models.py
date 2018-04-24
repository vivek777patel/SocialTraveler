from django.db import models

# Create your models here.
# from __future__ import unicode_literals

from django.db import models


class StaticInfo(models.Model):
    combo_type_choices = (
        ('G', 'Gender',),
        ('L', 'Location',),
        ('P', 'Photo_type',),
        ('M', 'Media_type')
    )
    combo_type = models.CharField(max_length=1,choices=combo_type_choices,)
    static_info_id = models.AutoField(primary_key=True)
    #combo_type = models.CharField(max_length=200, null=False)
    value = models.CharField(max_length=200, null=False)


    is_active = models.IntegerField(default=1, null=False)
#
# class Value(models.Model):
#     value = models.CharField(max_length=200, null=False)
#     value_for = models.ForeignKey(StaticInfo)

    def __str__(self):
        """A string representation of the model."""
        return self.value
