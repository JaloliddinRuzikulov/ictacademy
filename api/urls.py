from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = [
    path('mentors/', MentorsListView.as_view()),
    path('mentors/<int:pk>/', MentorsRetrieveView.as_view()),
    path('courses-category/', CourseCategoryListView.as_view()),
    path('courses/', CoursesListView.as_view()),
    path('courses/<int:pk>', CoursesRetrieveView.as_view()),
    path('feedback/', FeedbackListView.as_view()),
    path('feedback/<int:pk>', FeedbackRetrieveView.as_view()),
    path('projects/', ProjectsListView.as_view()),
    path('projects/<int:pk>', ProjectsRetrieveView.as_view()),
    path('article-category/', ArticleCategoryListView.as_view()),
    path('article/', ArticleListView.as_view()),
    path('article/<int:pk>/', ArticleRetrieveView.as_view()),
    

    path('contact/', ContactCreateView.as_view()),
    path('company/', CompanysListView.as_view()), ]
