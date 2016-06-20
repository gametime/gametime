from django.contrib import admin
from website.models import Terrain, Sport

class TerrainAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'lieu', 'sport', 'etat')
    list_filter    = ('sport', 'etat')
    search_fields  = ('nom', 'lieu')

admin.site.register(Sport)
admin.site.register(Terrain, TerrainAdmin)
