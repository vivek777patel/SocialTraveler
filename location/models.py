import datetime
from django.db import models

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
    address_line2 = models.CharField(max_length=200, null=False)
    address_line3 = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    latitude = models.DecimalField(max_digits=19, decimal_places=10);
    longitude = models.DecimalField(max_digits=19, decimal_places=10);
    updated_time = models.DateTimeField(auto_now=True, auto_now_add=False, default=datetime.date.today)
    # Map it to static info once it is merged
    # user_id = models.ForeignKey(User, related_name='user', null=False, on_delete=models.CASCADE)
    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return '{0} ({1})'.format(self.user_status_id, self.user_id.email)


