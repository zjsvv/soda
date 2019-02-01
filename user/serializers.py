from django.contrib.auth import authenticate
from django.db.models import Q
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username_or_email'

    def validate(self, attrs):

        password = attrs.get("password")
        user_queryset = User.objects.filter(
            Q(email__exact=attrs.get("username_or_email")) |
            Q(username__exact=attrs.get("username_or_email"))
        )
        if user_queryset.exists():
            user_obj = user_queryset.first()
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)
