from healthCheck.application.repositories.healthCheckRepository import HealthCheckRepository
from healthCheck.application.responses.healthCheckResponse import HealthCheckResponse

class HealthCheckUsecase:
    def handle(self):
        repository = HealthCheckRepository()
        currentDate = repository.getCurrentDate()

        healthCheckResponse = HealthCheckResponse().getHealthCheck(currentDate)
        return healthCheckResponse
