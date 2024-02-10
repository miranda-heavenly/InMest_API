from django.contrib import admin
from users.models import *

# Register your models here.
class IMUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user_type", "date_created")

class CohortAdmin(admin.ModelAdmin):
    list_display=("name", "year", "author", "date_created")

class CohortMemberAdmin(admin.ModelAdmin):
    list_display=("cohort", "member", "date_created")

admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohorMember)
