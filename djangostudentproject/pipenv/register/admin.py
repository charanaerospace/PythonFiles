from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display =('id','first_name','last_name','department','email', 'mobile','semester')
    list_display_links =('id','first_name','last_name','department','email', 'mobile','semester')
    
admin.site.register(Student, StudentAdmin)    