from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user(request):
    user = request.user
    serialized_user = CustomUserSerializer(user, many=False)
    return Response(serialized_user.data)
