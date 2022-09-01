from .models import Appeals
from rest_framework import serializers

class AppealSerializer(serializers.ModelSerializer):
    crime_id = serializers.IntegerField()
    crime_type = serializers.CharField()
    report_date = serializers.DateField()
    call_date = serializers.DateField()
    offense_date = serializers.DateField()
    call_time = serializers.TimeField()
    call_datetime = serializers.DateTimeField()
    disposition = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    agency_id = serializers.IntegerField()
    address_type = serializers.CharField()
    common_location = serializers.CharField()

    class Meta:
        model = Appeals
        fields = "__all__"