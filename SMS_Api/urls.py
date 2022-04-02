from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# from Api_one import views
from SMS_Api.views import *

urlpatterns = [
    path('students', StudentList.as_view()),
    path('teacher/<int:pk>', TeacherDetail.as_view()),
    path('subject/<int:pk>', SubjectDetail.as_view()),
    path('teachers', TeachersList.as_view()),
    path('subjects', SubjectsList.as_view()),
    path('classes', ClassesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
