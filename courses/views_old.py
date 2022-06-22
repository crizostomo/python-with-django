from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Appraisal
from .serializers import SerializerCourse, SerializerAppraisal


class CourseAPIView(APIView):
    """
    API - Courses
    """

    def get(self, request):
        courses = Course.objects.all()
        serializer = SerializerCourse(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SerializerCourse(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def put(self, request, pk=None, format=None):
    #     courses = Course.objects.get(pk=pk)
    #     serializer = SerializerCourse(courses, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppraisalAPIView(APIView):
    """
    API - Appraisals
    """

    def get(self, request):
        appraisals = Appraisal.objects.all()
        serializer = SerializerAppraisal(appraisals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SerializerAppraisal(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
