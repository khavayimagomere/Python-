from django.contrib import admin
from Mywebsite.models import Blog, Reader
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','comments', 'course']
admin.site.register(Blog, BlogAdmin)

class ReaderAdmin(admin.ModelAdmin):
    list_display = ['About', 'contact']
admin.site.register(Reader, ReaderAdmin)




    






