from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:patient_id>/', views.get_conversation, name='conversation'),
    path('<uuid:conversation_id>/message/', views.create_message, name='create_message'),
    path('<uuid:conversation_id>/messages/', views.get_messages, name='get_message'),
    path('<uuid:message_id>/edit/', views.update_message, name='update_message'),
    path('<uuid:message_id>/delete/', views.delete_message, name='delete_message'),
    path('', views.get_conversations, name='get_conversations'),

]
