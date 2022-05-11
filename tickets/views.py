from customuser.models import User
from rest_framework import generics, permissions  # , viewsets
from rest_framework.exceptions import ValidationError
from tickets.models import Ticket
from tickets.serializers import TicketSerializer

# class TicketViewSet(viewsets.ModelViewSet):

#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

#     def get_permissions(self):
# #User can create new tickets and see existing ones, but can't change them
#         if self.request.method == 'GET' or self.request.method == 'POST':
#             self.permission_classes = [permissions.IsAuthenticated, ]
#         else:
# #Admin can change ticket(status principally)
#             self.permission_classes = [permissions.IsAdminUser, ]

#         return super(TicketViewSet, self).get_permissions()

#     def perform_create(self, serializer):
#         author = User.objects.get(id=self.request.user.id)
#         serializer.save(author=author)

class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )

class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        author = User.objects.get(id = self.request.user.id)
        serializer.save(author=author)

class TicketRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        author = User.objects.get(id = self.request.user.id)
        if self.request.user.is_support:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError({'Error': 'No permission(only for author and support'})


#отдельная вьюха для обновления тикета
# class TicketUpdate(generics.UpdateAPIView):
#     """
#     Обновление только статуса заявки
#     """

#     serializer_class = TicketUpdateSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         if self.request.user.is_support:
#             return Ticket.objects.all()
