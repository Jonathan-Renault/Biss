from biss_app.api import serializers
from watchmate_app.models import WatchM, PlatformM, ReviewM
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewM
        fields = ['id', 'name', 'review', 'watch', 'created', 'updated', ]


class WatchSerializer(serializers.ModelSerializer):
    watchlist = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchM
        fields = ['id', 'title', 'description', 'watchlist', 'platform', 'created', 'updated', ]


class PlatformSerializer(serializers.ModelSerializer):
    platform = WatchSerializer(many=True, read_only=True)

    class Meta:
        model = PlatformM
        fields = ['id', 'name', 'site', 'platform', 'created', 'updated', ]
