import pytest
from customuser.models import User
from django.contrib.auth import get_user_model


@pytest.fixture
def test_user(db) -> User:

    User = get_user_model()
    testuser = User.objects.create_user(username='testuser',
                                        password='askjdfjkad')
    testuser.save()
    return testuser


def test_created_user(test_user):

    assert User.objects.filter(username="testuser").exists()
    assert test_user.username == 'testuser'
    assert test_user.is_support == False


def test_updated_user(test_user):
    test_user.is_support = True
    test_user.save()
    user_from_db = User.objects.get(username='testuser')
    assert user_from_db.is_support == True
