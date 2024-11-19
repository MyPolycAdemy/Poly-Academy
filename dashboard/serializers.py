from rest_framework import serializers
from .models import CourseModel, LessonModel, LayoutModel, MultipleChoiceModel, TrueOrFalseModel, OrderingTaskModel, CategoriesTaskModel, FillInTheGapsTaskModel

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ['id', 'course_name', 'description', 'category', 'level', 'bullet_points', 'img_cover', 'scorm_version', 'created_at', 'updated_at']


class LessonModelSerializer(serializers.ModelSerializer):
    course = CourseModelSerializer(read_only=True)  # Nested serializer for course information
    
    class Meta:
        model = LessonModel
        fields = ['id', 'lesson_name', 'description', 'course', 'bullet_points', 'img_cover', 'scorm_version', 'created_at', 'updated_at']


class LayoutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayoutModel
        fields = ['id', 'title', 'instructions', 'img_cover', 'audio', 'audio_script']


class MultipleChoiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceModel
        fields = ['id', 'layout', 'instructions', 'question', 'answers', 'order']


class TrueOrFalseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueOrFalseModel
        fields = ['id', 'layout', 'instructions', 'questions', 'order']


class OrderingTaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderingTaskModel
        fields = ['id', 'layout', 'instructions', 'items', 'order']


class CategoriesTaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesTaskModel
        fields = ['id', 'layout', 'instructions', 'categories', 'order']


class FillInTheGapsTaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillInTheGapsTaskModel
        fields = ['id', 'layout', 'instructions', 'text_with_gaps', 'keywords', 'order']
