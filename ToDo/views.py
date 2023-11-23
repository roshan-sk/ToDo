from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import filters
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class TaskListView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Firstname']

    def GetData(request):
        data=Task.objects.all()
        serializer=TaskSerializer(data, many=True)
        return Response(serializer.data)

    def AddData(request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def Task_details(request, id):
        try:
            data = Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TaskSerializer(data)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = TaskSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # refresh = RefreshToken.for_user(User)
            return Response({"status":200,"message ":"user added successfully", "data": serializer.data['username']})
        else:
            return Response({"status":200, "message":"User already existing"})