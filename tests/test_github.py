import allure
from allure_commons.types import Severity
from selene import browser, by, be, have


def test_git_with_selene():
    browser.open("https://github.com/")
    browser.element(".header-search-input").set_value("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#76")).should(have.text("#76"))


def test_git_with_allure_steps():
    allure.dynamic.tag("hw")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.epic("qa guru")
    allure.dynamic.feature("Allure reports")
    allure.dynamic.story("test with allure steps")
    allure.dynamic.link("https://github.com", name="Testing")

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


def test_git_with_allure_decorator_steps():
    allure.dynamic.tag("hw")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.epic("qa guru")
    allure.dynamic.feature("Allure reports")
    allure.dynamic.story("test with allure decorator steps")
    allure.dynamic.link("https://github.com", name="Testing")
    open_browser_page()
    search_repo("eroshenkoam/allure-example")
    go_to_repo("eroshenkoam/allure-example")
    go_to_issues()
    check_issue("#76")


@allure.step("Открываем страницу в браузере")
def open_browser_page():
    browser.open("https://github.com/")


@allure.step("Ищем репозиторий {repo}")
def search_repo(repo):
    browser.element(".header-search-input").set_value(repo)
    browser.element(".header-search-input").submit()


@allure.step("Переходим в репозиторий {repo}")
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Переходим в Issues")
def go_to_issues():
    browser.element("#issues-tab").click()


@allure.step("Проверка необходимого issue {nubmer}")
def check_issue(number):
    browser.element(by.partial_text(number)).should(have.text(number))

