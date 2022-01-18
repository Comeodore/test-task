import time

import pytest
from framework.page_actions import Page_Actions
from framework.sidebar import SideBar

s = SideBar()


@pytest.mark.parametrize('element_name', ['addHub', 'settings', 'help', 'logs', 'rules'])
def test_sidebar_elements(driver, login, check_sidebar_element, write_log, element_name):
    p = Page_Actions(driver)
    p.click_on_element(s.menuButton)
    time.sleep(1)
    write_log('Looking for "' + element_name + '" in SideBar')
    if check_sidebar_element(element_name, p.find_els_by_cls(s.menuClass)):
        write_log('Element "' + element_name + '" in SideBar')
        assert True
    else:
        write_log('Element "' + element_name + '" not in SideBar')
        assert True
    p.close_connection()
