from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from teatimeapi.models import TeaType


class TeaTypeView(ViewSet):
    """Tea Type View"""

    def list(self, request):
        """Handle GET requests to get tea types

        Returns:
            Response -- JSON serialized event
        """
        teatypes = TeaType.objects.all()

        serializer = TeaTypeSerializer(teatypes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single tea type
        Returns:
        Response -- JSON serialized tea"""
        tea = TeaType.objects.get(pk=pk)
        serializer = TeaTypeSerializer(tea)
        return Response(serializer.data)


class TeaTypeSerializer(serializers.ModelSerializer):
    """JSON Serializer for Tea Types"""
    class Meta:
        model = TeaType
        fields = ("id", "tea_type", "image",)
