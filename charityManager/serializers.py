from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from .models import NgoMaster,NgoType,UserMaster,UserPref,CharityType
from django.contrib.auth.models import User

class NgoMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model = NgoMaster
          fields = ('ngo_name','ngo_phone','ngo_city','ngo_state','ngo_fund')
          
class NgoTypeSerializer(serializers.ModelSerializer):
    class Meta:
          model = NgoType
          fields = ('ngo','ngo_type')

class CharityTypeSerializer(serializers.ModelSerializer):
    class Meta:
          model = CharityType
          fields = ('name','desc')
          
class UserMasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
          model = UserMaster
          fields = ('user_name','user_phone','user_wallet')
          
class UserPrefSerializer(serializers.ModelSerializer):
    class Meta:
          model = UserPref
          fields = ('user','user_pref')
          
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','pk','password', 'username', 'email', 'is_staff']

          