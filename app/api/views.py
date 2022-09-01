from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Appeals
from .serializers import AppealSerializer

class AppealListView(generics.ListAPIView):
    serializer_class = AppealSerializer

    def get_queryset(self):
        queryset = Appeals.objects.all()
        
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if date_from is not None:
            queryset = queryset.filter(report_date__gte=date_from)
        if date_to is not None:
            queryset = queryset.filter(report_date__lte=date_to)

        queryset = queryset.order_by("-report_date", "-call_time")
        return queryset