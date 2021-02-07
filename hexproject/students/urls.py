from django.urls import path


from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('students/<int:id>/' , views.studentview , name = 'studentview'),
    path('students/', views.students , name ='students'),
    path('students/list/' , views.studentslist , name = 'list'),
    path('students/update/<str:pk>/' , views.updatestudent , name ='updatestudent'),
    path('students/delete/<str:pk>/' , views.deletestudent , name ='deletestudent'),
    path('search/' , views.searchbar , name='search'),
]
