from django.contrib import admin
from .models import Mentors,  Feedback, Projects, AboutUs
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'company')
admin.site.register(Mentors)
admin.site.register(Projects)
admin.site.register(AboutUs)
admin.site.register(Feedback, FeedbackAdmin)