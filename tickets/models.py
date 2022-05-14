from django.db import models


class Ticket(models.Model):
    """
    Model of Ticket with limited options for
    field 'status'
    """
    class TicketStatus(models.TextChoices):
        ACTIVE = 'Active'
        FROZEN = 'Frozen'
        SOLVED = 'Solved'

    status = models.CharField(max_length = 25, choices = TicketStatus.choices,
                              default = TicketStatus.ACTIVE,
                              )

    title = models.CharField(max_length=200)
    author = models.ForeignKey('customuser.User', on_delete=models.CASCADE, )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
