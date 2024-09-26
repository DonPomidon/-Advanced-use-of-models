from django.urls import path
from . import views


app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teacher, name='teachers'),
    path('class_details/', views.class_detail, name='class_details'),
    path('students/', views.student, name='students'),
    path('adult_student/', views.adult_student, name='adult_students'),
    path('young_students/', views.young_student, name='young_students'),
]
