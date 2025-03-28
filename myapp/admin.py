from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session_year)
admin.site.register(StaffNotifications)
admin.site.register(Feedback)
