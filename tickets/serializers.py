from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)


class TicketSerializer(serializers.ModelSerializer):
  #Display User's username instead of bare id
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        read_only_fields = ('status',)
        fields = ('id', 'status', 'title', 'author',
                  'body', 'created', 'updated', )
        model = Ticket
