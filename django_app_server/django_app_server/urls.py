from django.urls import path
from .views import PerformanceTestApiView

urlpatterns = [
    path('', PerformanceTestApiView.as_view()),
]
