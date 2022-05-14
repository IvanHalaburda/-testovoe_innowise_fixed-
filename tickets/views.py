from customuser.models import User
from rest_framework import generics, permissions  # , viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from tickets.models import Ticket
from tickets.serializers import TicketSerializer, TicketUpdateSerializer


class TicketListView(generics.ListAPIView):
    """
    Displays all tickets if User was authenticated
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )


class TicketCreateView(generics.CreateAPIView):
    """
    Creates ticket, populates field 'author'
    with current User
    """
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        author = User.objects.get(id=self.request.user.id)
        serializer.save(author=author)


class TicketRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    Displays information about Ticket and allows
    author and support user to delete Ticket
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        author = User.objects.get(id=self.request.user.id)
        if self.request.user.is_support or instance.author == author:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError({'Error':
                                   'No permission (only for author and support)'})


class TicketUpdateView(generics.UpdateAPIView):
    """
    Updating Ticket's status.
    Allowed only to support user
    """

    serializer_class = TicketUpdateSerializer

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()
        else:
            raise ValidationError({'Error':
                                  'No permission (only for support)'})
