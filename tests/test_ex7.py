import pytest
from selenium.webdriver.chrome import options
from selenium import webdriver

from django.test import LiveServerTestCase



# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome('./chromedriver')
#         driver.get(("%s%s" % (self.live_server_url, '/admin/login/')))
#         assert "Log in | Django site admin" in driver.title


# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         option = webdriver.ChromeOptions()
#         option.add_argument('--headless')
#         driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, '/admin/login/')))
#         assert "Log in | Django site admin" in driver.title


# @pytest.fixture(scope="class")
# class chrome_driver_init(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close

# @pytest.mark.usefixtures(chrome_driver_init)
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, '/admin/login/')))
#         assert "Log in | Django site admin" in self.driver.title


# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver_init(requset):
#     if request.params == "chrome":
#         web_driver = webdriver.Chrome(executable_path=r"./chromedriver")
#     if request.params == "firefox":
#         web_driver = webdriver.Firefox(executable_path=r"./geckodriver")
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

@pytest.mark.usefixtures(driver_init)
class Test_URL_Chrome(LiveServerTestCase):
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (self.live_server.url, '/admin/')))
        assert "Log in | Django site admin" in self.driver.title



