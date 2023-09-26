from django.contrib import admin
from .models import NonTeachingStaff


class NonTeachingStaffAdmin(admin.ModelAdmin):
    list_display = ("non_teaching_staff_id",
                    "phone_number",
                    "school",
                    "user",
                    )
    

admin.site.register(NonTeachingStaff, NonTeachingStaffAdmin)

# Register your models here.
