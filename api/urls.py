from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = []

urlpatterns += [

    path('about/', AboutRetrieveView.as_view()),
    path('contact/', ContactRetrieveView.as_view()),
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
    path('article/<int:pk>', ArticleRetrieveView.as_view()),
    

    path('kursga-yozilish', KursgaYozilishCreateView.as_view()),
    # path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    # path('category-update/<int:pk>', views.BookCategoryUpdateView.as_view()),
    # path('category-retrieve-update/<int:pk>', views.BookCategoryRetrieveUpdateView.as_view()),
    # path('category-delete/<int:pk>', views.BookCategoryDestroyView.as_view()),
]
