from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import permissions

from .models import Course, Appraisal
from .serializers import SerializerCourse, SerializerAppraisal
from .permissions import IsSuperUser


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
    permission_classes = (
        IsSuperUser, #The order here matters
        permissions.DjangoModelPermissions, )
    queryset = Course.objects.all()
    serializer_class = SerializerCourse

    @action(detail=True, methods=['get'])
    def appraisals(self, request, pk=None):
        self.pagination_class.page_size = 2 # Defining manually the pagination for the route 'appraisals'
        appraisals = Appraisal.objects.filter(course_id=pk)
        page = self.paginate_queryset(appraisals)

        if page is not None:
            serializer = SerializerAppraisal(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SerializerAppraisal(appraisals, many=True)
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
