from django.contrib import admin
from .models import CourseCategory, Courses, Contact
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk','category', 'name','course_length', 'modules', 'lessons')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'profession', 'phone', 'date')

admin.site.register(CourseCategory)
admin.site.register(Courses, CourseAdmin)
admin.site.register(Contact, ContactAdmin)