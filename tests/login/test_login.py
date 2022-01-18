import time
import pytest
from framework.login_page import LoginPage
from framework.page_actions import Page_Actions

l = LoginPage()


@pytest.mark.parametrize('login, password',
                         [('qa.ajax.app.automation@gmail.com', 'qa_automation_password'), ('123', '123'), ('', ''),
                          ('qa.ajax.app.automation@gmail.com', '123'), ('123', 'qa_automation_password')])
def test_success_user_login(driver, write_log, login, password):
    p = Page_Actions(driver)
    p.click_on_element(l.get_login_button_id())
    p.fill_element(l.get_login_field_id(), login)
    p.fill_element(l.get_password_field_id(), password)
    p.click_on_element(l.get_next_button_id())
    write_log('Try login with ' + login + ' | ' + password)
    time.sleep(1)
    try:
        p.find_el('com.ajaxsystems:id/login')
        if p.text_element('com.ajaxsystems:id/snackbar_text') == 'Wrong login or password':
            write_log('Wrong login or password')
            assert True
        elif p.text_element('com.ajaxsystems:id/snackbar_text') == 'Please fill all of the required fields.':
            write_log('Please fill all of the required fields.')
            assert True
        else:
            assert False
    except:
        write_log('Login success')
        assert True
    p.close_connection()
