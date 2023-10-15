from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response

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
        movie_detail = Movie.objects.get(pk=pk)
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
            return Response(status=204)