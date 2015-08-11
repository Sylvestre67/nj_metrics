from django.contrib import admin
from metrics import models

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.County)
admin.site.register(models.Party)
admin.site.register(models.Election)

