from rest_framework import serializers
import api.models as am


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Book
        fields = '__all__'
