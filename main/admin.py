from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

class RoomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)

class ContainerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','room__name']
    list_display = ('name','room')

class SubContainerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','container__name']
    list_display = ('name','container',)

class ObjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','subContainer__name']
    list_display = ('name','subContainer','public',)

class ViewLogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ('id','user','object','last_seen')

admin.site.register(Room, RoomAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(SubContainer, SubContainerAdmin)
admin.site.register(Object, ObjectAdmin)
admin.site.register(ViewLog, ViewLogAdmin)