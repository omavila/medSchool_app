from django.contrib import admin
from .models import Client, Notegroup, Notecard
# Register your models here.

admin.site.register(Client)
admin.site.register(Notecard)
admin.site.register(Notegroup)