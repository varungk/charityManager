from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

router = routers.DefaultRouter()
router.register(r'userdetails', UserRegisterViewSet)
router.register(r'users', UserViewSet)
router.register(r'userpref', UserPrefRegisterViewSet)
router.register(r'ngo', NgoRegisterViewSet)
router.register(r'ngotype', NgoTypeRegisterViewSet)
router.register(r'charity', CharityTypeViewSet)

urlpatterns = [
    path('register/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
]
