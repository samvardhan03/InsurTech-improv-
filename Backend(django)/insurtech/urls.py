# insurtech-backend/insurtech/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('insurance_app.urls')),
]