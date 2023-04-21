from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializers(ModelSerializer):
    class META:
        model = User
        fields = ['username'].__getattribute__