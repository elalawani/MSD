# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(
        'upload_measurement/',
        views.upload_measurement,
        name='upload_measurement'
    ),
    path(
        'get_all_measurements/<uuid:patient_id>',
        views.get_all_measurements,
        name='get_all_measurements'
    ),
    path(
        'create_measurement_comment/',
        views.create_measurement_comment,
        name='create_measurement_comment'
    ),
    path(
        'get_measurement_comments/<uuid:patient_id>/',
        views.get_measurement_comments,
        name='get_measurement_comments'
    ),
]
