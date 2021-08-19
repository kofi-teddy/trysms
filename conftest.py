import pytest
from selenium import webdriver

from django.test import LiveServerTestCase

# from pytest_factoryboy import register

# from tests.factories import UserFactory, CategoryFactory, ProductFactory


# register(UserFactory)
# register(CategoryFactory)
# register(ProductFactory)

# @pytest.fixture
# def new_user1(db, user_factory):
#     user = user_factory.create()
#     return user


# @pytest.fixture(scope="class")
# class chrome_driver_init(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(requset):
    if request.params == "chrome":
        web_driver = webdriver.Chrome(executable_path=r"./chromedriver")
    if request.params == "firefox":
        web_driver = webdriver.Firefox(executable_path=r"./geckodriver")
    request.cls.driver = web_driver
    yield
    web_driver.close()
