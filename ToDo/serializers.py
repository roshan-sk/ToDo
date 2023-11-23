from rest_framework import serializers
from .models import Task
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','Firstname','Lastname','Email','Age']

    validators = [
            UniqueTogetherValidator(
                queryset=Task.objects.all(),
                fields=['Email'],
            )
        ]
