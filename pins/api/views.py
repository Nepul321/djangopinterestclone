from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import ImagePin
from rest_framework.permissions import (
    IsAuthenticated
)

from .serializers import ImagePinSerializer

@api_view(['GET'])
def ImagePinsListView(request, *args, **kwargs):
    imagepins = ImagePin.objects.filter(is_private=False)
    serializer = ImagePinSerializer(imagepins, many=True)
    data  = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
def ImagePinDetailView(request, id, *args, **kwargs):
    user = request.user
    qs = ImagePin.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Not found"}, status=404)
    obj = qs.first()
    if obj.is_private == True and user != obj.user:
        return Response({"detail" : "You can't view this post"}, status=403)
    serializer = ImagePinSerializer(obj)
    data = serializer.data
    
    return Response(data, status=200)

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def ImagePinCreateView(request, *args, **kwargs):
    data = request.data
    serializer = ImagePinSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(
            user=request.user
        )
        return Response(serializer.data, status=201)
    
    return Response({}, status=401)