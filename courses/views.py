from rest_framework import generics

from .models import Course, Appraisal
from .serializers import SerializerCourse, SerializerAppraisal


class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = SerializerCourse


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = SerializerCourse


class AppraisalsAPIView(generics.ListCreateAPIView):
    queryset = Appraisal.objects.all()
    serializer_class = SerializerAppraisal


class AppraisalAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appraisal.objects.all()
    serializer_class = SerializerAppraisal