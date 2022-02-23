from django.db import connection
from healthCheck.domain.entities.healthCheck import HealthCheckEntity

class HealthCheckRepository:
    def getCurrentDate(self) -> HealthCheckEntity:
        with connection.cursor() as cursor:
            cursor.execute("SELECT NOW() AS `CURRENT_DATE`")
            row = cursor.fetchone()
                
        healthCheck = HealthCheckEntity(row[0])
        return healthCheck
