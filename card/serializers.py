from rest_framework import serializers

from .models import FlashCard

class CreateFlashCardSerializer(serializers.ModelSerializer) :

    class Meta :
        
        model = FlashCard

        fields = '__all__'

class UpdateFlashCardSerializer(serializers.ModelSerializer) :

    class Meta :
        model = FlashCard

        fields = ('question' , 'answer')


class DeleteFlashCardSerializer(serializers.ModelSerializer) :

    class Meta :
        model = FlashCard
        fields = '__all__'



class ListFlashCardSerializer(serializers.ModelSerializer) :

    class Meta :

    
        model = FlashCard
    
        fields = '__all__'