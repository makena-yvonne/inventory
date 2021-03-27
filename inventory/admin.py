from django.contrib import admin
from .models import *

# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(Kitchenware, Chicken)
class ViewAdmin(admin.ModelAdmin):
    pass