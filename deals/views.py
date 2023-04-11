# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

from .models import Deal
from .serializers import DealSerializer

class DealListApiView(APIView):
    authentication_classes = [TokenAuthentication]

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # List all
    def get(self, request, *args, **kwargs):
        deals = Deal.objects.filter(user = request.user.id)
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Deal with given deal data
        '''
        data = {
            'task': request.data.get('title'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = DealSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)