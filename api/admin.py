from django.contrib import admin
from .models import Movie

class MovieList(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating', 'director', 'movie_image')
    list_filter = ('name', 'year', 'rating', 'director', 'movie_image')
    search_fields = ('name', 'description')
    ordering = ['year']

admin.site.register(Movie, MovieList)
