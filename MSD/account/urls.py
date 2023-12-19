from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<uuid:user_id>/', views.update_profile, name='update_profile'),
    path('profile/address/<uuid:user_id>/', views.update_address, name='update_address'),
    path('signup/', views.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('nurses/', views.nurse_list, name='nurse_list'),

]
