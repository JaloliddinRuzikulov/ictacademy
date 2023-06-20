from rest_framework import serializers
from apps.about.models import Mentors,  Feedback, Projects, AboutUs
from apps.blog.models import ArticleCategory, Article
from apps.course.models import CourseCategory, Courses, Contact, EnrollCourse



class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = ('name', 'profession', 'github', 'linkedin', 'telegram', 'instagram', 'image')


 
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


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class EnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollCourse
        fields = '__all__'


class CompanysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('company','company_logo')
