from rest_framework import serializers
from apps.about.models import Mentors,  Feedback, Projects
from apps.blog.models import ArticleCategory, Article
# from apps.contact.models import Contact
from apps.course.models import CourseCategory, Courses, Contact



class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentors
        fields = ('name', 'profession', 'github', 'linkedin', 'telegram', 'instagram')


 
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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'





class CompanysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('company','company_logo')

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.company_logo:
    #         representation['company_logo'] = instance.company_logo.url
    #     return representation

    # def get_filtered_queryset(self):
    #     queryset = self.Meta.model.objects.filter(company_logo__isnull=False)
    #     return queryset