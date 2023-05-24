from rest_framework import serializers
from apps.about.models import Mentors, About, Feedback, Projects
from apps.blog.models import ArticleCategory, Article
from apps.contact.models import Contact
from apps.course.models import CourseCategory, Courses, KursgaYozilish



class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = '__all__'


 
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class KursgaYozilishSerializer(serializers.ModelSerializer):
    class Meta:
        model = KursgaYozilish
        fields = '__all__'
