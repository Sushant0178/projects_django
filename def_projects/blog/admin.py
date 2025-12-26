from django.contrib import admin
from .models import Blogg , Comment

# Register your models

admin.site.register(Blogg)
admin.site.register(Comment)