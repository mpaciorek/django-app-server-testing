from django.urls import path
from .views import PerformanceTestApiView

urlpatterns = [
    path('api/', PerformanceTestApiView.as_view()),
]
