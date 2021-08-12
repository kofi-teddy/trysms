from django.contrib import admin, auth
from django.urls import path
from . views import home, auth_view, verify_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_view, name='login-view'),
    path('verify/', verify_view, name='verify-view'),
]
