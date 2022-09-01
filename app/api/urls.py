from django.urls import path, include

from .views import AppealListView


urlpatterns = [
    path('list/', AppealListView.as_view()),
]
