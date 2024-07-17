from abc import ABC

from rest_framework import serializers


class Get_Name(serializers.Serializer):
    name = serializers.CharField()
