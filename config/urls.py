from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('customuser.urls')),
    path('api/v1/', include('tickets.urls')),
#Display messages related to ticket, which id == pk
    path('api/v1/<int:pk>/', include('answers.urls')),
]
