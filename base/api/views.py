from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def APIBASEPOINT(request, *args, **kwargs):
    return Response([], status=200)