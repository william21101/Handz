from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import TextSerializer, UserSerializer
from rest_framework.views import APIView

from .models import Text
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth import get_user_model
User = get_user_model()

class TextView(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = (IsAuthenticated,)

class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class LoginView(APIView):
    def post(self, request):
        user = User.objects.get(username=request.data["username"])
        user.is_logged_in = True
        user.save()

        return Response({"message": "Success"})

class LogoutView(APIView):
    def post(self, request):
        user = User.objects.get(auth_token=request.data["token"])
        user.is_logged_in = False
        user.save()

        return Response({"message": "Success"})


def testview(request):
    return render(request, 'test.html', {})
