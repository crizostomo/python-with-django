from django.contrib import admin

from .models import Course, Appraise

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation', 'update', 'active')

@admin.register(Appraise)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'appraisal', 'creation', 'update', 'active')
