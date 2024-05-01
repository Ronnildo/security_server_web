from django.contrib import admin

from .models import Data, User
# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']