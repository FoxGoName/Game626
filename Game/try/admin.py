from django.contrib import admin
from .models import Game, Image, Jurisdiction
# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image

class JurisdictionInline(admin.TabularInline):
    model = Jurisdiction

class GameAdmin(admin.ModelAdmin):
    inlines = [ImageInline, JurisdictionInline]

admin.site.register(Game, GameAdmin)


admin.site.register(Image)
admin.site.register(Jurisdiction)