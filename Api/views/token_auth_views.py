from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate


class LoginAPIView(APIView):
    def post(self, request):
        username =  request.data.get('username')
        password =  request.data.get('password')

        if not username or not password:
            return Response({'error': 'Both username and password is required.'}, status=HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'massage': 'invalid credentials.'}, status=HTTP_401_UNAUTHORIZED)
        
        return Response({'massage': 'User logned in successfully.'})


class LogOutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail': 'logged out successfully'})