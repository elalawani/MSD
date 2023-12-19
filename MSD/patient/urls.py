from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('filtered/', views.patient_list_filtered, name='patient_list_filtered'),
    path('<uuid:pk>/', views.patient, name='patient'),
    path('create/', views.add_patient, name='add_patient'),
    path('<uuid:pk>/edit/', views.edit_patient, name='edit_patient'),
    path('<uuid:pk>/delete/', views.delete_patient, name='delete_patient'),

]
