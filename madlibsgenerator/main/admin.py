from django.contrib import admin

# Register your models here.

from .models import BaseText, Substitution

admin.site.register(BaseText)
admin.site.register(Substitution)
