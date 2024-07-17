from rest_framework.generics import GenericAPIView
import logging
from cicd_app import serializers
from rest_framework.response import Response


class MorningAPI(GenericAPIView):
    serializer_class = serializers.Get_Name

    def post(self, request, *args, **kwargs):
        txt = f'Have a Great day {request.data["name"]}!!!!'
        txt2 = f'You are selected for the role {request.data["role"]}'
        return Response(
            txt,
            txt2
        )
