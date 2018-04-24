from django.contrib import admin

# Register your models here.
from .models import User, UserStatus, UserFriends

admin.site.register(User)
admin.site.register(UserStatus)
admin.site.register(UserFriends)
