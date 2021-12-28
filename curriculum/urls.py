from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [
    path('', views.StandardListView.as_view(), name='standard_list'),
    path('course/', views.courseListView.as_view(), name='course_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    # path('<str:standard>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('course/<int:pk>/', views.LessonListView.as_view(), name='courselesson'),

    path('<str:standard>/<str:slug>/create/', views.LessonCreateView.as_view(),name='lesson_create'),
    path('<str:standard>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(),name='lesson_detail'),
    path('lesson/<str:pk>/', views.Lesson2DetailView.as_view(),name='lesson2_detail'),
    path('<str:standard>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(),name='lesson_update'),
    path('<str:standard>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(),name='lesson_delete'),

    # casting 
    
    path('section/<slug:slug>/',views.sec_list_def, name='section'),
    path('section/course/<int:slugid>/<slug:slug>/',views.sec_cou_list_def, name='sec_cou'),

]
