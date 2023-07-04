import pytest
from allure_commons.types import Severity
from selene import browser
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
import allure

@allure.label('owner', 'a.rassokhin')
@allure.tag('web', 'auto')
@allure.severity(Severity.NORMAL)
@allure.feature('Тесты для гитхаба с шагами')
@allure.story('decorator')

def test_github():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)