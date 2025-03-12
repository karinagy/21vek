from django.urls import path

from apps.main.api.views.distance_calculator_views import CalculatorAPIView

urlpatterns = [
    path("calculate/", CalculatorAPIView.as_view(), name="distance-calculator"),
]
