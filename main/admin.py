from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)

class ContainerAdmin(admin.ModelAdmin):
    search_fields = ['name','room__name']
    list_display = ('name','room')

class SubcontainerAdmin(admin.ModelAdmin):
    search_fields = ['name','container__name']
    list_display = ('name','container',)

class ObjectAdmin(admin.ModelAdmin):
    search_fields = ['name','subcontainer__name']
    list_display = ('name','subcontainer','public',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Subcontainer, SubcontainerAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(ViewLog)