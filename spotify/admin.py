from django.contrib import admin
from .models import SpotifyToken, Vote

admin.site.register(SpotifyToken)
admin.site.register(Vote)
