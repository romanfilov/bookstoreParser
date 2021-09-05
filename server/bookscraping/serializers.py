from rest_framework import serializers


class BookStoreSerializer(serializers.Serializer):
    author = serializers.CharField()
    price = serializers.IntegerField()
    name = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
