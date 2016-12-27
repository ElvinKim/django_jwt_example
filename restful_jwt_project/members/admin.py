from django.contrib import admin
from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', "last_mod_date", "reg_date")

admin.site.register(Member, MemberAdmin)


