import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.person_page import PersonPage
from pages.recovery_page import RecoveryPage
from pages.register_page import RegisterPage
from pages.video_page import VideoPage
from pages.home_page import HomePage
from utils.client import load_config, get_chrome_options, URL, VIDEO, PERSON, LOGIN, RESET, REGISTER


@pytest.fixture
def driver() -> webdriver:
    config: dict = load_config()
    options: Options = get_chrome_options(config["chrome_options"])
    driver: webdriver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver: webdriver) -> HomePage:
    driver.get(URL)
    return HomePage(driver)


@pytest.fixture
def video_page(driver: webdriver) -> VideoPage:
    driver.get(VIDEO)
    return VideoPage(driver)


@pytest.fixture
def person_page(driver: webdriver) -> PersonPage:
    driver.get(PERSON)
    return PersonPage(driver)


@pytest.fixture
def login_page(driver: webdriver) -> LoginPage:
    driver.get(LOGIN)
    return LoginPage(driver)


@pytest.fixture
def recovery_page(driver: webdriver) -> RecoveryPage:
    driver.get(RESET)
    return RecoveryPage(driver)


@pytest.fixture
def register_page(driver: webdriver) -> RegisterPage:
    driver.get(REGISTER)
    return RegisterPage(driver)
