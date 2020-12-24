from django.contrib import admin

# Register your models here.
from capital.models import Capital


class CapitalAdmin(admin.ModelAdmin):
    list_display = ("ativo", "valor")


admin.site.register(Capital, CapitalAdmin)
