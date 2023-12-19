from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')),
    path('api/patients/', include('patient.urls')),
    path('api/conversation/', include('conversation.urls')),
    path('api/documentation/', include('documentation.urls')),
    path('api/sensor/', include('sensor.urls')),
    path('api/todo/', include('todolist.urls')),
    path('api/questionnaires/', include('questionnaires.urls')),
    path('api/measure_fhir/', include('measure_fhir.urls')),
    path('admin/', admin.site.urls),
]
