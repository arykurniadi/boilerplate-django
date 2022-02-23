from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
from healthCheck.views import HealthCheckView

urlpatterns = [
    url(r'^boilerplate/health-check$', HealthCheckView.as_view(), name="health-check"),    
]