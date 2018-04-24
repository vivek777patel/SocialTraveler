# Create your models here.

from django.db import models


class StaticInfo(models.Model):
    class Meta:
        app_label = 'static_info'
        db_table = "static_info"

    static_info_id = models.AutoField(primary_key=True)
    combo_type = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null=False)
    is_active = models.IntegerField(default=1, null=False)

    def __str__(self):
        """A string representation of the model."""
        return self.value
