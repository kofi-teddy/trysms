import pytest


from apps.users.models import CustomUser as User


# def test_new_user(user_factory):
#     print(user_factory.username)
#     assert True

# def test_new_user(user_factory):
#     user = user_factory.build()
#     print(user.username)
#     assert True


# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.create()
#     count = User.objects.all().count()
#     print(user.username)
#     print(count)
#     assert True

# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.build()
#     count = User.objects.all().count()
#     print(user.username)
#     print(count)
#     assert True

# def test_new_user(new_user1):
#     print(new_user1.username)
#     assert True

def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert True
