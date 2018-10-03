from django.contrib import admin
from .models import planet,padawan_bd,jedi_bd,candidate,test
# Register your models here.
admin.site.register(planet)
admin.site.register(padawan_bd)
admin.site.register(jedi_bd)
admin.site.register(candidate)
admin.site.register(test)