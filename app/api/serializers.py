from rest_framework import serializers


class TestObjectSerializer(serializers.Serializer):
    """Serializes a sample JSON object"""
    name = serializers.CharField()
    age = serializers.IntegerField()
    occupation = serializers.CharField()

# 1. MetadataLedgerSerializer

# 2. SupplementalLedgerSerializer
