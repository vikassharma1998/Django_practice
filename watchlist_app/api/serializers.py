from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Movie name must greater than 5 characters")
        return value
    def validate(self, data):
        if data['name'] == data['descriptions']:
            raise serializers.ValidationError("Movie name and description must be different")
        return data