from django.contrib import admin
from forumapp.models import Student, Empathy

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']
admin.site.register(Student, StudentAdmin)

class EmpathyAdmin(admin.ModelAdmin):
    list_display = ['location', 'trainer']
admin.site.register(Empathy, EmpathyAdmin)

