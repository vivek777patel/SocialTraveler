from django.contrib import admin

# Register your models here.
from .models import User, UserStatus

admin.site.register(User)
admin.site.register(UserStatus)
