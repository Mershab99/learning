from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from db.models import User

from db.serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users':'/users/',
        'Detail Users':'/user/<int:pk>/',
        'Create':'/user-create/',
        'Modify':'/user-update/<int:pk>/',
        'Delete':'/user-delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    parser_class = (FileUploadParser,)
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def userDelete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('User succesfully deleted!')