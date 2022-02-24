from django.contrib import admin
from .models import *

admin.site.register(Room)
admin.site.register(Container)
admin.site.register(Subcontainer)
admin.site.register(Object)
admin.site.register(ViewLog)