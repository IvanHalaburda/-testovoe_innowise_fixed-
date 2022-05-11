from django.urls import path
from tickets.views import (TicketCreateView, TicketListView,
                           TicketRetrieveDeleteView)

urlpatterns = [
    path('tickets/', TicketListView.as_view()),
    path('tickets/<int:pk>/', TicketRetrieveDeleteView.as_view()),
    path('tickets/create/', TicketCreateView.as_view()),

]

# from rest_framework.routers import SimpleRouter
# from tickets.views import TicketViewSet

# router = SimpleRouter()
# router.register('', TicketViewSet, basename='tickets')

# urlpatterns = router.urls
