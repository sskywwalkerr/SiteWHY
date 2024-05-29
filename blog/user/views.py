from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView





class UserByToken(APIView):

    def post(self,request, format=None):
        data = {
            'id': str(request.user.id),
            'username': str(request.user.username),
            'email': str(request.user.email),

        }
        return Response(data=data, status=status.HTTP_201_CREATED)