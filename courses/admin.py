from django.contrib import admin

from .models import Course, Appraisal

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation', 'update', 'active')

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'appraisal', 'creation', 'update', 'active')
