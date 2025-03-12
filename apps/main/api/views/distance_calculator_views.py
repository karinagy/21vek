from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.main.api.serializers.distance_calculator_serializers import (
    DistanceCalculatorSerializer,
)
from apps.main.services.distance_calculator import DistanceCalculatorService


@extend_schema(
    request=DistanceCalculatorSerializer,
    parameters=[
        OpenApiParameter(
            name="library_mode",
            description="Параметр задается для получения решения с использованием алгоритма или кастомного",
            required=False,
            type=bool,
        )
    ],
)
class CalculatorAPIView(APIView):
    def post(self, request):
        serializer = DistanceCalculatorSerializer(data=request.data)
        if serializer.is_valid():
            words = serializer.validated_data["words"]
            library_mode = request.query_params.get("library_mode", "false").lower() == "true"

            distance = DistanceCalculatorService.calculate(words, library_mode)

            return Response({"distance": distance}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
