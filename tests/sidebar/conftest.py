import time

import pytest
from framework.page_actions import Page_Actions
from framework.login_page import LoginPage

l = LoginPage()


@pytest.fixture
def login(driver):
    p = Page_Actions(driver)
    p.click_on_element(l.get_login_button_id())
    p.fill_element(l.get_login_field_id(), 'qa.ajax.app.automation@gmail.com')
    p.fill_element(l.get_password_field_id(), 'qa_automation_password')
    p.click_on_element(l.get_next_button_id())
    time.sleep(3)
    p.click_on_element('com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    p.click_on_element('com.ajaxsystems:id/cancel_button')


def _check_sidebar_element(el_name, elements):
    for i in elements[2:]:
        if i.get_attribute('resource-id').split('/')[1] == el_name:
            return True
    return False


@pytest.fixture
def check_sidebar_element():
    return _check_sidebar_element
