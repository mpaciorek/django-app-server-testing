from rest_framework.views import APIView
from rest_framework.response import Response


class PerformanceTestApiView(APIView):
    """
       View to list all users in the system.

       * Requires token authentication.
       * Only admin users are able to access this view.
    """
    def post(self, request, *args, **kwargs):
        return Response([])

    def get(self, request, *args, **kwargs):
        return Response({'status': 'ok'})