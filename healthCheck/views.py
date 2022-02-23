from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from healthCheck.application.useCases.healthCheckUsecase import HealthCheckUsecase

class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        usecase = HealthCheckUsecase().handle()

        payload = usecase.data
        return Response(data=payload, status=status.HTTP_200_OK, content_type="application/json")