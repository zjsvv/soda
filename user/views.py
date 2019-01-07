from rest_framework import mixins, viewsets

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
