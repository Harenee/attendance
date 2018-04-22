from django.urls import path

from . import views
app_name = 'polls'

urlpatterns = [
    path('polls/', views.polls, name='polls'),
    path('create_student/', views.create_student, name = 'create_student'),
    path('create_staff/', views.create_staff, name = 'create_staff'),
    path('create_subject/', views.create_subject, name = 'create_subject'),
    path('detail/', views.detail, name='detail'),
]
