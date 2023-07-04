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
@allure.story('labda')

def test_github():
    with allure.step("Открыть главную страницу GitHub"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Кликаем по табу Issue"):
        s("#issues-tab").click()

    with allure.step("Находим нужный номер"):
        s(by.partial_text("#76")).should(be.visible)