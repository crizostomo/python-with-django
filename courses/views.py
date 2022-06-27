from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Course, Appraisal
from .serializers import SerializerCourse, SerializerAppraisal

"""
API V1
"""


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


"""
AP1 V2
"""


class ViewSetCourse(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = SerializerCourse

    @action(detail=True, methods=['get'])
    def appraisals(self, request, pk=None):
        course = self.get_object()
        serializer = SerializerAppraisal(course.appraisals.all(), many=True)
        return Response(serializer.data)


"""
class ViewSetAppraisal(viewsets.ModelViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = SerializerAppraisal
"""


class ViewSetAppraisal(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    queryset = Appraisal.objects.all()
    serializer_class = SerializerAppraisal
