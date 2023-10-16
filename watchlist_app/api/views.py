from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status


class MovieListAV(APIView):
    def get(self,request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)
    def post(self, request):
        movie = MovieSerializer(data= request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=201)
        else:
            return Response(movie.errors, status=400)

class MovieDetailsAV(APIView):
    def get(self,request,pk):
        try:
            movie_detail = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie does not exist'},status=status.HTTP_404_NOT_FOUND)    
        serializer = MovieSerializer(movie_detail)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie_detail = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self,request,pk):
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({'status_reason':'Deleted'},status=status.HTTP_204_NO_CONTENT)