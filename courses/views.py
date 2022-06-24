from rest_framework import generics
from rest_framework.generics import get_object_or_404

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

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class AppraisalAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appraisal.objects.all()
    serializer_class = SerializerAppraisal

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(),
                                     course_id=self.kwargs.get('course_pk'),
                                     pk=self.kwargs.get('appraisal_pk'))
        return get_object_or_404(self.get_queryset(),
                                 pk=self.kwargs.get('appraisal_pk'))
