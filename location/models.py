import datetime
from django.db import models
from user.models import User
# Create your models here.

'''
    vivek777patel
'''


class LocationInfo(models.Model):

    class Meta:
        app_label = 'location'
        db_table = "location_info"

    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=200, null=False)
    address_line1 = models.CharField(max_length=200, null=False)
    address_line2 = models.CharField(max_length=200, blank=True)
    address_line3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=False, blank=True)
    zip_code = models.CharField(max_length=200, null=False, blank=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10)
    longitude = models.DecimalField(max_digits=19, decimal_places=10)
    updated_time = models.DateTimeField(auto_now=True)
    # Map it to static info once it is merged
    # user_id = models.ForeignKey(User, related_name='user', null=False, on_delete=models.CASCADE)
    review = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return self.location_name


class LocationDetails(models.Model):

    class Meta:
        app_label = 'location'
        db_table = "location_details"

    location_details_id = models.AutoField(primary_key=True)
    photo_link = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    location_det_info = models.ForeignKey(LocationInfo, related_name='location_det_info', null=False, on_delete=models.CASCADE)

    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return '{0} : {1} : {2} : {3}'.format(self.location_det_info.location_id, self.location_det_info.location_name, self.description, self.photo_link)


class VisitedLocationInfo(models.Model):

    class Meta:
        app_label = 'location'
        db_table = "visited_location"
        ordering = ["-updated_time"]

    visited_location_id = models.AutoField(primary_key=True)
    updated_time = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, related_name='visited_location_user', null=False, on_delete=models.CASCADE)
    location_id = models.ForeignKey(LocationInfo, related_name='location_info', null=False, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return '{0}: {1} | {2} : {3} | {4}'.format(self.user_id.id, self.user_id.email, self.location_id.location_id, self.location_id.location_name, self.updated_time)
