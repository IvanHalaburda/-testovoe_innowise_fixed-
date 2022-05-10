from customuser.models import User
from rest_framework import permissions, viewsets
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


class TicketViewSet(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_permissions(self):
#User can create new tickets and see existing ones, but can't change them
        if self.request.method == 'GET' or self.request.method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated, ]
        else:
#Admin can change ticket(status principally)
            self.permission_classes = [permissions.IsAdminUser, ]

        return super(TicketViewSet, self).get_permissions()

    def perform_create(self, serializer):
        author = User.objects.get(id=self.request.user.id)
        serializer.save(author=author)
