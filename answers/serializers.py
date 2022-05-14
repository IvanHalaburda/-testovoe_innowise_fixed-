from answers.models import Message
from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class AuthorSerializer(serializers.ModelSerializer):
    """
    This serializer being used to return User's
    username instead of bare id
    """
    class Meta:
        model = get_user_model()
        fields = ('username', 'is_support')


class TicketTitleSerializer(serializers.ModelSerializer):
    """
    This serializer being used to return Ticket's
    title instead of bare id
    """
    class Meta:
        model = Ticket
        fields = ('title', )


class MessageSerializer(serializers.ModelSerializer):
    """
    Provides information about message
    """
    author = AuthorSerializer(many=False, read_only=True)
    related_ticket = TicketTitleSerializer(many=False, read_only=True)

    class Meta:
        fields = ('id', 'body', 'related_ticket', 'author', 'created', )
        model = Message
