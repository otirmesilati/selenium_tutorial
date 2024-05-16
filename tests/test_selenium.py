from selenium import webdriver
import pytest

@pytest.mark.my_selenium
def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    assert driver.title == "Selenium"
    driver.quit()