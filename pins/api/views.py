from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import ImagePin
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