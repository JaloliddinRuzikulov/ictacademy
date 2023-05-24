
from rest_framework import  generics
from rest_framework.response import Response
from .serializers import *
from .pagination import *
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




class ArticleCategoryListView(generics.ListAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer

class CourseCategoryListView(generics.ListAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer



# RETIRIEVE VIEW  => GET  (one)
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



# RETIRIEVE VIEW  => GET  (one)
class AboutRetrieveView(generics.RetrieveAPIView):
    def get(self, request):
        last_item = About.objects.last()
        serializer = AboutSerializer(last_item)
        return Response(serializer.data)
    
class ContactRetrieveView(generics.RetrieveAPIView):
    def get(self, request):
        last_item = Contact.objects.last()
        serializer = ContactSerializer(last_item)
        return Response(serializer.data)



# CREATE VIEW  => POST
class KursgaYozilishCreateView(generics.CreateAPIView):
    queryset = KursgaYozilish.objects.all()
    serializer_class = KursgaYozilishSerializer


# class MentorsListView(generics.ListAPIView):
#     queryset = Mentors.objects.all()
#     serializer_class = MentorSerializer

# # CREATE VIEW  => POST
# class BookCategoryCreateView(generics.CreateAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer

# # LIST CREATE VIEW  => GET  and   POST
# class BookCategoryListCreateView(generics.ListCreateAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer

# # RETIRIEVE VIEW  => GET  (one)
# class BookCategoryRetrieveView(generics.RetrieveAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer

# # Update VIEW  => PUT  (one)
# class BookCategoryUpdateView(generics.UpdateAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer

# # RETIRIEVE UPDATE VIEW  => GET  (one) and PUT
# class BookCategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer


# # DESTROY VIEW  => DELETE  (one)
# class BookCategoryDestroyView(generics.DestroyAPIView):
#     queryset = BookCategory.objects.all()
#     serializer_class = BookCategorySerializer
