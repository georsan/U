from django.contrib import admin
from .models import persona
from .models import tipodocumento
from .models import ciudad
#poder mostrar en sqlite
admin.site.register(persona)
admin.site.register(tipodocumento)
admin.site.register(ciudad)