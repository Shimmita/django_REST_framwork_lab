from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer
from rest_framework import mixins, generics
# Create your views here.

class AllUsersApiView(generics.GenericAPIView, mixins.ListModelMixin):
        #use Querryset
     queryset=UserModel.objects.all()
    #use serializer
     serializer_class= UserSerializer
     #fun fetch all user data
     def get(self, request):
         return self.list(request)
     
     
     
class SpecificUserApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    #use Querryset
    queryset=UserModel.objects.all()
    #use serializer
    serializer_class= UserSerializer
    
    #use id index in retrieving the specific user
    lookup_field='id'
    
    #fun to get all data and also to retrieve specific data of the user
    def get(self, request, id):
        if id:
         return self.retrieve(request)
    #fun  post a user to the backend database
    def post(self, request):
        return self.create(request)
    
    #fun update user record
    def put(self, request, id=None):
        return self.update(request, id)
    
    #fun delete user
    def delete(self, request, id=None):
        return self.destroy(request, id)
    