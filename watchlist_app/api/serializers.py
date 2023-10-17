from rest_framework import serializers
from watchlist_app.models import StreamPlatform, WatchList


class WatchListSerializers(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    # label = serializers.SerializerMethodField()
    # key = serializers.SerializerMethodField()
    watchlist = WatchListSerializers(many= True, read_only= True)
    class Meta:
        model = StreamPlatform
        fields =  '__all__'  #['label', 'key',]

    # def get_label(self, obj):
    #     return obj.name
    
    # def get_key(self, obj):
    #     return obj.pk
    
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Movie name must greater than 5 characters")
        return value
    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError("Movie name and about must be different")
        return data
    



    

    