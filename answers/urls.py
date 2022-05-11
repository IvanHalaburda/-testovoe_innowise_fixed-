from answers.views import MessageList
from django.urls import path

urlpatterns = [
    path('<int:pk>/messages/', MessageList.as_view()),
]
