from rest_framework.views import APIView

from .models import FlashCard
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 , get_list_or_404
from .serializers import (
    CreateFlashCardSerializer , 
    UpdateFlashCardSerializer,
    DeleteFlashCardSerializer,
    ListFlashCardSerializer
)

class CreateFlashCardView(APIView) :

    def post (self , request) :

        req_data = request.data
        serializer = CreateFlashCardSerializer(data = req_data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data , status = 201)


class UpdateFlashCardView(APIView) :

    def put (self, request , id) :

        req_data = request.data
        flash_card = get_object_or_404(FlashCard , id = id )
        serializer = UpdateFlashCardSerializer(instance = flash_card , data = req_data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
       
        return Response(serializer.data , status = 200)

class DeleteFlashCardView(APIView) :

    def delete(self , request , id ) :

        flash_card = get_object_or_404 (FlashCard , id = id) 
        flash_card.delete()
        return Response(status= 204)


class ListFlashCardView(APIView) :

    def get(self, request, user_id) :

        flash_card = get_list_or_404(FlashCard , user__id = user_id)
        serializer = ListFlashCardSerializer(flash_card , many = True)

        return Response(serializer.data) 
        

