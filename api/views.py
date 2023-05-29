
from rest_framework import  generics
from rest_framework.response import Response
from .serializers import *
from .pagination import *
import requests
# Create your views here.



#----------------------------- GENERIC VIEWS -----------------------#



# LIST VIEW  => GET
class MentorsListView(generics.ListAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorSerializer

class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class CoursesListView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class ProjectsListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CompanysListView(generics.ListAPIView):
    serializer_class = CompanysSerializer

    def get_queryset(self):
        queryset = Feedback.objects.all()
        query = []
        for q in queryset:
            if q.company_logo:
                query.append(q)
        return query

class ArticleCategoryListView(generics.ListAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer

class CourseCategoryListView(generics.ListAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer



# RETIRIEVE VIEW  => GET  
class MentorsRetrieveView(generics.RetrieveAPIView):
    queryset = Mentors.objects.all()
    serializer_class = MentorSerializer

class CoursesRetrieveView(generics.RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class FeedbackRetrieveView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ProjectsRetrieveView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ArticleRetrieveView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# CREATE VIEW  => POST
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

