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
    # Nested Relationship
    # appraisals = SerializerAppraisal(many=True, read_only=True)

    # HyperLinked Related Field
    # appraisals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='appraisal-detail')

    # Primary Key Related Field
    appraisals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'appraisals'
        )
