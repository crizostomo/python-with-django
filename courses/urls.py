from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CourseAPIView,
    CoursesAPIView,
    AppraisalAPIView,
    AppraisalsAPIView,
    ViewSetCourse,
    ViewSetAppraisal)

router = SimpleRouter()
router.register('courses', ViewSetCourse)
router.register('appraisals', ViewSetAppraisal)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/appraisals/', AppraisalsAPIView.as_view(), name='course_appraisals'),
    path('courses/<int:course_pk>/appraisals/<int:appraisal_pk>/', AppraisalAPIView.as_view(), name='course_appraisal'),

    path('appraisals/', AppraisalsAPIView.as_view(), name='appraisals'),
    path('appraisals/<int:appraisal_pk>/', AppraisalAPIView.as_view(), name='appraisal'),
]