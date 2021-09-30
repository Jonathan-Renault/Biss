from biss_app.models import History
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    res = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = History
        exclude = ('id', 'created',)
