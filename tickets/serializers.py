from django.contrib.auth import get_user_model
from rest_framework import serializers
from tickets.models import Ticket

from .tasks import status_update_notification


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


class TicketUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('status',)

    def update(self, instance, validated_data):
        changed_status = validated_data.get('status', instance.status)

        if instance.status != changed_status:
            instance.status = changed_status
            instance.save()
            status_update_notification.delay(instance.title, instance.author.email,
                                             changed_status)
        return instance
