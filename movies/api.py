from movies.models import Movies
from rest_framework import viewsets, permissions
from .serializer import MovieSerializer

# Lead Viewset (creates full crud program without explicitly making methods for functions)
class MovieViewSet(viewsets.ModelViewSet):
    querySet = Movies.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = MovieSerializer