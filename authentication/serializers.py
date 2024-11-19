from rest_framework import serializers
from django.contrib.auth.models import User



class CreateUserProfileSerializer(serializers.ModelSerializer) :

    class Meta :
        model = User 

        fields = ('id', 'username','email','password')

        extra_kwargs = {'password':{'write_only':True}}



    # def create(self, validated_data):
    #     """
    #     این متد کاربر جدیدی ایجاد می‌کند و رمز عبور را هش می‌کند
    #     """
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         password=validated_data['password']  # هش‌شدن رمز عبور
    #     )
    #     return user