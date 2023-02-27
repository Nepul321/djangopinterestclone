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