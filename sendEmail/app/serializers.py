from rest_framework import serializers
from .models import SendEmail


class SendEmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = SendEmail
        fields = "__all__"
