from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, TaskSerializer


class PerformanceTestApiView(APIView):
    """
       View to list all users in the system.

       * Requires token authentication.
       * Only admin users are able to access this view.
    """

    def get(self, request, *args, **kwargs):
        tasks = [
            Task(id=1, title='Demo', owner='test1', status='Done'),
            Task(id=2, title='Model less demo', owner='test2', status='InProgress'),
            Task(id=3, title='Model less demo', owner='test3', status='New'),
            Task(id=4, title='Demos', owner='test3', status='New'),
            Task(id=5, title='Test 01', owner='test3', status='New'),
            Task(id=6, title='Test 02', owner='test3', status='InProgress'),
            Task(id=7, title='test 03', owner='test3', status='New'),
            Task(id=8, title='Sleep more', owner='test3', status='Done')
        ]

        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)
