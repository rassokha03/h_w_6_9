import allure
import pytest
from allure_commons.types import Severity
from selene import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s

@allure.label('owner', 'a.rassokhin')
@allure.tag('web', 'auto')
@allure.severity(Severity.CRITICAL)
@allure.feature('Тесты для гитхаба с шагами')
@allure.story('decorator')

def test_steps():
    open_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    click_to_issues()
    should_see_issues_with_number("#76")

@allure.step("Открываем главную страницу github")
def open_page():
    browser.open("https://github.com")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()

@allure.step("Переходим в репозиторий{repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Кликаем по табу Issues")
def click_to_issues():
    s("#issues-tab").click()

@allure.step("Ищем нужный номер {number}")
def should_see_issues_with_number(number):
    s(by.partial_text(number)).click()