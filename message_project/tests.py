import pytest
import allure
from allure import attach, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime


def pytest_configure(config):
    config.addinivalue_line("markers", "positive: mark a test as positive test.")

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

@allure.feature('Генератор ЭУ')
@allure.story('Генерация сообщения и ссылки на ЭУ')
class TestEUMessageGeneration:
    
    @allure.title('Генерация сообщения для ЭУ')
    @pytest.mark.positive
    def test_success_eu_message_generation(self, driver):
        # driver.get('http://localhost:5000/')
        driver.get('https://amamam277.pythonanywhere.com/')
        name_input = driver.find_element(By.NAME, 'name')
        date_input = driver.find_element(By.NAME, 'date')

        name_input.send_keys('Иван')
        time.sleep(2)
        date_input.send_keys('22.04.2024 пн-11:00 (время МСК)')
        time.sleep(2)
        submit_button = driver.find_element(By.CLASS_NAME,'btn-primary')
        submit_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'message_done')))

        message = driver.find_element(By.ID, 'message_done').get_attribute('value')

        

        assert 'Меня зовут Амур, я преподаватель из школы программирования Kodland. Нам с Иваном назначили дополнительный экспертный урок для определения дальнейшего курса обучения. Время проведения: 22.04.2024 пн-11:00 (время МСК).' in message

    