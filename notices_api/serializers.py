from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Notices


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = '__all__'


