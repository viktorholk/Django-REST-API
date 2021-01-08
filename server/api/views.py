from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import seriallizers
from . import models
from . import permissions

class UserViewSet(viewsets.ModelViewSet):
    # Handles creating and updating users

    serializer_class        = seriallizers.UserSeriallizer
    queryset                = models.User.objects.all()
    authentication_classes  = ( TokenAuthentication, )
    permission_classes      = ( permissions.UpdateProfile, )
    filter_backends         = ( filters.SearchFilter, )
    search_fields           = ( 'email', 'username', )