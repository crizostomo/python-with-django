from rest_framework.views import APIView
from rest_framework.response import Response

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


class AppraisalAPIView(APIView):
    """
    API - Appraisals
    """

    def get(self, request):
        appraisals = Appraisal.objects.all()
        serializer = SerializerAppraisal(appraisals, many=True)
        return Response(serializer.data)
