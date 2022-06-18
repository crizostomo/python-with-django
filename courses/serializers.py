from rest_framework import serializers

from .models import Course, Appraisal


class SerializerAppraisal(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Appraisal
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'appraisal',
            'creation',
            'active'
        )


class SerializerCourse(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active'
        )
