import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


from abstract.selenium_listener import MyListener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headles if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1680,1050')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options

    # в версии selenium 4.0.0 выдает предупреждение что этот метод скоро уберут
    # driver = webdriver.Chrome(
    #     executable_path='C:/Users/stepa/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/Scripts/chromedriver.exe',
    #     options=options)
    # return driver

    ser = Service(
        'C:/Users/stepa/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/Scripts/chromedriver.exe')
    s = webdriver.Chrome(service=ser, options=options)
    return s
#


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, MyListener())
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()  # удаляем куки чтобы обойти защиту сайта
    yield driver
    driver.quit()
