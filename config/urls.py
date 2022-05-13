from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('customuser.urls')),
    path('api/v1/', include('tickets.urls')),
    path('api/v1/tickets/', include('answers.urls')),
]
