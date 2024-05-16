from selenium import webdriver
import pytest


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    assert driver.title == "selenium"
    driver.quit()