from time import time
from healthCheck.domain.entities.healthCheck import HealthCheckEntity
from rest_framework import serializers

class GetHealthCheckSerializer(serializers.Serializer):
    timestamp = serializers.CharField()

class HealthCheckResponse:
    def getHealthCheck(self, healthCheck: HealthCheckEntity) -> GetHealthCheckSerializer:
        healthCheckResponse = GetHealthCheckSerializer(healthCheck)
        return healthCheckResponse
