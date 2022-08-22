import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # use headles if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1680,1050')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    # path ""C:\Users\stepa\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9\Scripts\chromedriver.exe""
    options = get_chrome_options
    ser = Service(
        'C:/Users/stepa/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/Scripts/chromedriver.exe')
    s = webdriver.Chrome(service=ser, options=options)
    return s





@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies() # удаляем куки чтобы обойти защиту сайта
    yield driver
    driver.quit()
