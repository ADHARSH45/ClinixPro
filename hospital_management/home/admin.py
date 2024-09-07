from django.contrib import admin

# Register your models here.
from .models import departments,doctor,booking

admin.site.register(departments)
admin.site.register(doctor)
admin.site.register(booking)
