from rest_framework import serializers
from courses.models import Subject, Course, Module, Content

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["title", "slug"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["owner", "subject", "title", "slug", "overview"]


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["course", "title", "description", "order"]


