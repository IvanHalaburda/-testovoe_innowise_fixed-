import pytest
from answers.models import Message
from django.contrib.auth import get_user_model
from tickets.models import Ticket


@pytest.fixture
def test_ticket_answer(db) -> Message:

    User = get_user_model()
    testuser = User.objects.create_user(username='testuser',
                                        password='askjdfjkad')
    testuser.save()
    testticket = Ticket.objects.create(status='Active', title='problem',
                                       author=testuser, body='problems')
    testticket.save()
    testanswer = Message.objects.create(related_ticket=testticket,
                                        author=testuser, body='answer')
    testanswer.save()
    return testanswer


def test_created_ticket(test_ticket_answer):

    assert Ticket.objects.filter(title="problem").exists()
    assert test_ticket_answer.body == 'answer'
    assert test_ticket_answer.author.username == 'testuser'
    assert test_ticket_answer.related_ticket.status == 'Active'


def test_updated_ticket(test_ticket_answer):
    test_ticket_answer.body = 'answer №2'
    test_ticket_answer.save()
    answer_from_db = Message.objects.get(body='answer №2')
    assert answer_from_db.body == 'answer №2'
