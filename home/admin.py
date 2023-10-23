from django.contrib import admin

from home.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
