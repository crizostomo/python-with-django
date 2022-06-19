from django.urls import path

from .views import CourseAPIView, AppraisalAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('appraisals/', AppraisalAPIView.as_view(), name='appraisals'),
]