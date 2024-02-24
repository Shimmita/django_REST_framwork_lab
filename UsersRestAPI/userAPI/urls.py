from django.urls import path
from .views import SpecificUserApiView,AllUsersApiView

urlpatterns = [
     path('allUsersApiView/', AllUsersApiView.as_view()),
    path('specificUserApiView/<int:id>/', SpecificUserApiView.as_view())
    
]
