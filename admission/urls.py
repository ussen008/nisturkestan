from django.urls import path
from . import views

app_name = 'admission'

urlpatterns = [
    path('upload/', views.upload_files, name='upload_files'),
    path('upload/<int:id>/', views.student_detail, name='student_detail'),
    path('', views.main_page, name='main_page'),

]

