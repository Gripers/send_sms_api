from django.contrib import admin
from .models import *


class BurgerAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "price", "category", "created"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["burger", "total", "created", "phone"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "created"]


class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created"]


admin.site.register(Burgers, BurgerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
