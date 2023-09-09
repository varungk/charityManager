from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import NgoMasterSerializer,NgoTypeSerializer,UserMasterSerializer,UserPrefSerializer,UserSerializer,CharityTypeSerializer
from .models import NgoMaster,NgoType,UserMaster,UserPref,CharityType

# Create your views here.
class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    
class UserPrefRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserPref.objects.all()
    serializer_class = UserPrefSerializer
    
class NgoRegisterViewSet(viewsets.ModelViewSet):
    queryset = NgoMaster.objects.all()
    serializer_class = NgoMasterSerializer
    
class CharityTypeViewSet(viewsets.ModelViewSet):
    queryset = CharityType.objects.all()
    serializer_class = CharityTypeSerializer
    
class NgoTypeRegisterViewSet(viewsets.ModelViewSet):
    queryset = NgoType.objects.all()
    serializer_class = NgoTypeSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

