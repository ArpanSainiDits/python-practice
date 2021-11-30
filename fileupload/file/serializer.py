from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Profile


class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"