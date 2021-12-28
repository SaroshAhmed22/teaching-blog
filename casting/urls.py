from django.urls import path
from . import views

app_name='casting'
urlpatterns = [
    path('', views.tableView.as_view(), name='timetableurl'),
    
    path('oberecord/', views.oberecord_view.as_view(), name='oberecordurl'),
    
    path('lab/', views.labView.as_view(), name='laburl'),
    path('freett/', views.freettview, name='freetturl'),
    path('oberecordcourse/', views.obechart_def, name='oberecordcourseurl'),
    path('proj/', views.projView.as_view(), name='projurl'),
    
    path('freettlab/', views.freettlabview, name='freettlaburl'),
    # path('<slug:slug>/', views.timetable_view.as_view(), name=''),
    path('<int:roomid>/<int:slotid>/<int:pk>/', views.bookview.as_view(), name='bookurl'),
    path('<str:roomname>/<str:slottime>/<int:fttid>/<slug:slug>/', views.bookviewdef, name='bookurldef'),
    path('lab/<str:roomname>/<str:slottime>/<int:fttid>/<slug:slug>/', views.booklabviewdef, name='booklaburldef'),
    path('<int:roomname>/<int:slottime>/<int:slug>/', views.bookviewdef2, name='bookurldef2'),
    path('<str:roomname>/<str:slottime2>/<str:ok>/<int:fttid>/<slug:slug>/', views.bookdone, name='bookdoneurldef'),
    path('lab/<str:roomname>/<str:slottime2>/<str:ok>/<int:fttid>/<slug:slug>/', views.booklabdone, name='booklabdoneurldef'),
    path('okdone/',views.successbookdone, name= 'okdone'),
    path('okdonelab/',views.successbookdonelab, name= 'okdonelab'),

    
    path('sectt/<int:secid>/<slug:slug>',views.sec_tt_def, name= 'sectt'),
    # path(' bookdoned/', views.bookdone, name='bookdoneurldef'),
    # path('<str:standard>/<str:slug>/create/', views.LessonCreateView.as_view(),name='lesson_create'),
    # path('<str:standard>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(),name='lesson_detail'),
    # path('<str:standard>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(),name='lesson_update'),
    # path('<str:standard>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(),name='lesson_delete'),

]



