from django.db import models

# Create your models here.

class Appeals(models.Model):
    crime_id = models.IntegerField(verbose_name="Crime ID")
    crime_type = models.CharField(verbose_name="Original Crime Type Name", max_length=100)
    report_date = models.DateField(verbose_name="Report Date")
    call_date = models.DateField(verbose_name="Call Date")
    offense_date = models.DateField(verbose_name="Offense Date")
    call_time = models.TimeField(verbose_name="Call Time")
    call_datetime = models.DateTimeField(verbose_name="Call Date Time")
    disposition = models.CharField(verbose_name="Disposition", max_length=50, default="Not recorded")
    address = models.CharField(verbose_name="Address", max_length=100)
    city = models.CharField(verbose_name="City", max_length=100)
    state = models.CharField(verbose_name="State", max_length=50)
    agency_id = models.SmallIntegerField(verbose_name="Agency ID")
    address_type = models.CharField(verbose_name="Address Type", max_length=100)
    common_location = models.CharField(verbose_name="Common Location", max_length=100, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['-report_date'], name='report_date_idx'),
        ]