from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name','email','token','verification_status','authcode','create_time']


admin.site.register(Account,AccountAdmin)