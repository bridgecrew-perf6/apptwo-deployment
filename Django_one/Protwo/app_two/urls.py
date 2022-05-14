from django.urls import path
from app_two import views

# TEMPLATE TAGGING
app_name = 'app_two'

urlpatterns = [
    path('users/',views.users,name = 'user'),
    path('registration/',views.registration,name = 'register'),
    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name = 'logout'),
    path('special/',views.special,name = 'special'),
]