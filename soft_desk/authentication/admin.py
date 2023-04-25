from django.contrib import admin
from authentication.models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('password', 'username', 'first_name', 'last_name', 'email')


admin.site.register(UserModel, UserModelAdmin)
