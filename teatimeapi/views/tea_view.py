"""View module for handling requests about teas"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from teatimeapi.models import Teas


class TeaView(ViewSet):
    """Tea Detail view"""

    def list(self, request):
        """Handle GET requests to get teas

        Returns:
            Response -- JSON serialized event
        """
        teas = Teas.objects.all()

        serializer = TeaSerializer(teas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single tea
        Returns:
        Response -- JSON serialized tea"""
        tea = Teas.objects.get(id=pk)
        serializer = TeaSerializer(tea)
        return Response(serializer.data)


class TeaSerializer(serializers.ModelSerializer):
    """JSON Serializer for Teas"""
    class Meta:
        model = Teas
        fields = ("id", "name", "image", "origin", "tea_type",
                  "caffeine", "description", "color", "taste", )
