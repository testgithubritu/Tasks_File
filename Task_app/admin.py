from django.contrib import admin

from Task_app.models import UserProfile,Education,link

# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Education)

admin.site.register(link)