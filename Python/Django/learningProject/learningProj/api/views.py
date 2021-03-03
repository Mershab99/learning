from rest_framework.decorators import api_view
from rest_framework.response import Response

from db.models import User, Location

from db.serializers import UserSerializer, LocationSerializer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Users': '/users/',
        'Detail Users': '/user/<int:pk>/',
        'Create': '/user-create/',
        'Modify': '/user-update/<int:pk>/',
        'Delete': '/user-delete/<int:pk>/',


        'Locations': '/locations/',
        'Location Detail': 'location-create/<int:lat>/<int:lng>/',
        'Location Create': 'location-create/<int:lat>/<int:lng>/',
        'Location Update': 'location-update/<int:pk>/',
        'Location Delete': 'location-delete/<int:pk>/',

        'User Cards': '/user-cards/',
        'User Card': '/user-card/<int:pk>/',
        'User Card Create': '/user-card-create/',

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


@api_view(['GET'])
def locationList(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def locationDetail(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(location, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def locationCreate(request):
    serializer = LocationSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def locationUpdate(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(location, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def locationDelete(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()
    return Response("Successfully Deleted Location")

@api_view(['GET'])
def userCardList(request):
    userCardList = User.objects.all()

    serializer = UserCardSerializer(userCardList, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userCardDetail(request, pk):
    userCard = User.objects.get(id=pk)
    serializer = UserCardSerializer(userCard, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCardCreate(request):
    serializer = UserCardSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)
