import allure
from selene import browser, by, be, have

def test_git_with_selene():
    browser.open("https://github.com/")
    browser.element(".header-search-input").set_value("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(have.text("#76"))

def test_git_with_allure_step():
    with allure.step("Открываем страницу в браузере"):
        browser.open("https://github.com/")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-input").set_value("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Переходим в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переходим в Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверка необходимого # issue"):
        browser.element(by.partial_text("#76")).should(have.text("#76"))


