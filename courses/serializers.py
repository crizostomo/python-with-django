from rest_framework import serializers
from django.db.models import Avg #Avg = Average

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

    def validate_appraisal(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError("The appraisal needs to be a full number and needs to be between 1 and 5")


class SerializerCourse(serializers.ModelSerializer):
    # Nested Relationship
    # appraisals = SerializerAppraisal(many=True, read_only=True)

    # HyperLinked Related Field
    # appraisals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='appraisal-detail')

    # Primary Key Related Field
    appraisals = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    average_appraisals = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'creation',
            'active',
            'appraisals',
            'average_appraisals'
        )

    def get_average_appraisals(self, obj):
        average = obj.appraisals.aggregate(Avg('appraisal')).get('appraisal__avg')

        if average is None:
            return 0
        return round(average * 2) / 2
