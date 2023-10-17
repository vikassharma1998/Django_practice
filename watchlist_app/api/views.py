from rest_framework.views import APIView
from watchlist_app.models import StreamPlatform, WatchList, Review
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializers, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status

class StreamPlatformAV(APIView):
    def get(self, request):
        stream_platform = StreamPlatform.objects.all()
        streamplatformserializer = StreamPlatformSerializer(stream_platform, many = True)
        
        return Response(streamplatformserializer.data, status=status.HTTP_202_ACCEPTED)
    
    def post(self, request):
        stream_platformserializer = StreamPlatformSerializer(data=request.data)
        if stream_platformserializer.is_valid():
            stream_platformserializer.save()
            return Response(stream_platformserializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(stream_platformserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatfromDetalisAV(APIView):
    def get(self,request,pk):
        try:
            stream_platform_details = StreamPlatform .objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
                return Response({'Error':'Stream Platfrom does not found'}, status= status.HTTP_404_NOT_FOUND)    
        streamplatformserializer = StreamPlatformSerializer(stream_platform_details)   

        return Response(streamplatformserializer.data)
        
    def put(self, request, pk):
           
            stream_platform_details = StreamPlatform .objects.get(pk=pk) 
            streamplatformserializer = StreamPlatformSerializer(stream_platform_details, data = request.data)
            if streamplatformserializer.is_valid():
               streamplatformserializer.save()

               return Response(streamplatformserializer.data)
            else:

                return Response(streamplatformserializer.errors)
            
    def delete(self, request, pk):
        stream_platform_details = StreamPlatform .objects.get(pk=pk) 
        stream_platform_details.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WatchListAV(APIView):
     def get(self, request):
          watchlist = WatchList.objects.all()
          watchlistserializers = WatchListSerializers(watchlist, many=True)

          return Response(watchlistserializers.data)
     
     def post(self, request):
        watchlistserializers = WatchListSerializers(data = request.data)
        if watchlistserializers.is_valid():
            watchlistserializers.save()
            return Response(watchlistserializers.data, status= status.HTTP_201_CREATED)
        else:
            return Response(watchlistserializers.errors)
     
class WatchListDetailsAV(APIView):

    def get(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlistserializer = WatchListSerializers(watchlist)   

        return Response(watchlistserializer.data)   
     
    def put(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlistserializer = WatchListSerializers(watchlist, data = request.data)  
        if watchlistserializer.is_valid():
            watchlistserializer.save()

            return Response(watchlistserializer.data)
        else:
            return Response(watchlistserializer.errors)
        
    def delete(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()

        return Response(status= status.HTTP_204_NO_CONTENT)


class ReviewAV(APIView):
    def get(self, request):
        review = Review.objects.all()
        review_serializer = ReviewSerializer(review, many=True)

        return Response(review_serializer.data)
    
    def post(self, request):
        review_serializer = ReviewSerializer(data=request.data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response(review_serializer.data)
        
class ReviewDetailsAV(APIView):

    def get(self, request,pk):
        try:
            review= Review.objects.get(pk=pk)
            review_serializer = ReviewSerializer(review)
            return Response(review_serializer.data)
        except Review.DoesNotExist:
            return Response({'Error': "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        review_serializer = ReviewSerializer(review, data=request.data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response(review_serializer.data)
        else :
             return Response(review_serializer.errors)      
        
    def delete(self, request,pk):
        review = Review.object.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    