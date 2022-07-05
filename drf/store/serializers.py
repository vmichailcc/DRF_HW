from rest_framework import serializers
from store.models import Store


class StoreSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.IntegerField()

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store
