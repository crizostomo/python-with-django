from django.urls import path

from .views import CourseAPIView, CoursesAPIView, AppraisalAPIView, AppraisalsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('appraisals/', AppraisalsAPIView.as_view(), name='appraisals'),
    path('appraisals/<int:pk>', AppraisalAPIView.as_view(), name='appraisal'),
]