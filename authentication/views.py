# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from authentication.serializers import CreateUserProfileSerializer
from rest_framework.response import  Response


class CreateUser(APIView) :

    def post(self ,request ) :

        req_data = request.data
        serializer = CreateUserProfileSerializer(data = req_data)
        serializer.is_valid(raise_exception = True)
        data = serializer.validated_data
        user_data = User(
            username = data['username'],
            email = data['email'],
        )

        user_data.set_password(data['password'])
        user_data.save()
        return Response(serializer.data)



# class CreateUser (CreateAPIView) :

#     queryset = User.objects.all()
#     serializer_class = CreateUserProfileSerializer
