from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)
    if request.method == 'POST':
        movie = MovieSerializer(data= request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=201)

@api_view(['GET','PUT','DELETE'])
def movie_details(request, pk):
    if request.method == 'GET':
        try:
            movie_detail = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie does not exist'},status=status.HTTP_404_NOT_FOUND)    
        serializer = MovieSerializer(movie_detail)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie_detail = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    if request.method == 'DELETE':
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({'status_reason':'Deleted'},status=status.HTTP_204_NO_CONTENT)