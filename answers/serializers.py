from answers.models import Message
from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'is_support')

class TicketTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('title', )

class MessageSerializer(serializers.ModelSerializer):
    User = get_user_model()
    author = AuthorSerializer(many=False, read_only=True)
    related_ticket = TicketTitleSerializer(many=False, read_only=True)
#Display User's username instead of id
    #author = serializers.SlugRelatedField(slug_field='username',
    #                                     queryset=User.objects.all())

#Display title of related ticket instead of id
    #related_ticket = serializers.SlugRelatedField(slug_field='title',
    #                                       queryset=Ticket.objects.all())

    class Meta:
        #read_only_fields = ('author', )
        fields = ('id', 'body', 'related_ticket', 'author', 'created', )
        model = Message
