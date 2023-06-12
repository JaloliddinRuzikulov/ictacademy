from django.contrib import admin

from .models import CourseCategory, Courses, Contact, EnrollCourse

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('category', 'name','course_length', 'modules', 'lessons',)
class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'courseid', 'phone', 'date',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date',)

admin.site.register(CourseCategory)
admin.site.register(Courses, CourseAdmin)

admin.site.register(Contact, ContactAdmin)
admin.site.register(EnrollCourse, EnrollCourseAdmin)
