from answers.serializers import MessageSerializer
from customuser.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from tickets.models import Ticket


class MessageList(generics.ListCreateAPIView):
#Quryset consists of messages, related to ticket with specific id 
    def get_queryset(self):
        related_ticket = get_object_or_404(Ticket, pk=self.kwargs['pk'])
        queryset = related_ticket.messages.all()
        return queryset
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        related_ticket = get_object_or_404(Ticket, pk = self.kwargs['pk'])
        author = User.objects.get(id = self.request.user.id)
        if self.request.user.is_support or author == related_ticket.author.id:
            serializer.save(author=author, related_ticket = related_ticket)
        else:
            raise ValidationError({'Error': 'No permission (only for author and support)'})
