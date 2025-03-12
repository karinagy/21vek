from rest_framework import serializers


class DistanceCalculatorSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField(max_length=255), min_length=2, max_length=2
    )

    def validate_words(self, value):
        return [word.strip() for word in value]
