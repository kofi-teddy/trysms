import pytest

from apps.users.models import CustomUser



# @pytest.fixture()
# def user1(db):
#     return CustomUser.objects.create_user('test-user')

# @pytest.mark.django_db
# def test_set_check_password(user1):
#     user1.set_password('new-password')
#     assert user1.check_password('new-password') is True


# def test_set_check_password(user1):
#     print('check-user1')
#     assert user1.username == 'test-user'

# def test_set_check_password1(user1):
#     print('check-user2')
#     assert user1.username == 'test-user'


# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == 'MyName'

# def test_new_user(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff