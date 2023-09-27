from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from rest_framework import status


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET/api",
        "GET/api/rooms",
        "GET/api/rooms/:id",
        "POST/api/room"
    ]
    return Response(routes)


@api_view(["GET"])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createRoom(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#    {
#         "id": 20,
#         "name": "TESTTTT",
#         "description": "lets learn the basics",
#         "host": 2,
#         "topic": 3,
#         "participants": []
#     }