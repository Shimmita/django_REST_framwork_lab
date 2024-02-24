from .models import UserModel
from rest_framework import serializers

#serializing the model in order to make it support json formats
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model=UserModel
       fields=['firstname', 'lastname', 'email']