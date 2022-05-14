import pytest
from django.contrib.auth import get_user_model
from tickets.models import Ticket


@pytest.fixture
def test_ticket(db) -> Ticket:

    User = get_user_model()
    testuser = User.objects.create_user(username='testuser',
                                        password='askjdfjkad')
    testuser.save()
    testticket = Ticket.objects.create(status='Active', title='problem',
                                       author=testuser, body='problems')
    testticket.save()
    return testticket


def test_created_ticket(test_ticket):

    assert Ticket.objects.filter(title="problem").exists()
    assert test_ticket.title == 'problem'
    assert test_ticket.status == 'Active'
    assert test_ticket.author.username == 'testuser'
    assert test_ticket.body == 'problems'


def test_updated_ticket(test_ticket):
    test_ticket.title = 'No problem'
    test_ticket.save()
    ticket_from_db = Ticket.objects.get(title='No problem')
    assert ticket_from_db.title == 'No problem'
