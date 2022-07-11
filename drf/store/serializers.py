from rest_framework import serializers
from store.models import Store



class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = [
            "id",
            "title",
            "description",
            "rating",
            "owner",
            "status",
        ]
        read_only_fields = ["owner", "status"]
