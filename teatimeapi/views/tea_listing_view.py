"""View module for handling requests about teas"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from teatimeapi.models import TeaListing


class TeaListingView(ViewSet):
    """Tea Listing view"""

    def list(self, request):
        """Handle GET requests to get teas

        Returns:
            Response -- JSON serialized event
        """
        teas = TeaListing.objects.all()

        serializer = TeaSerializer(teas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handle GET requests for single cocktail
        Returns:
        Response -- JSON serialized cocktail"""
        tea = TeaListing.objects.get(id=pk)
        serializer = TeaSerializer(tea)
        return Response(serializer.data)


class TeaSerializer(serializers.ModelSerializer):
    """JSON Serializer for Teas"""
    class Meta:
        model = TeaListing
        fields = ("id", "name", "image",)
