from django.contrib import admin
from .models import NTT, NNTName, CityName, Streets, Blog, Grant, NormativHujjat, OAV,Index
from django.contrib.auth.models import Group, User

admin.site.register(NTT)
admin.site.register(NNTName)
admin.site.register(CityName)
admin.site.register(Streets)
admin.site.register(Blog)
admin.site.register(Grant)
admin.site.register(NormativHujjat)
admin.site.register(OAV)
# admin.site.register(Index)


admin.site.unregister(Group)
admin.site.unregister(User)