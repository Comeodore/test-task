import time
import datetime
import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture
def driver():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    time.sleep(1)
    return driver


def _get_current_time():
    return str(datetime.datetime.now().strftime("[%d-%m-%Y - %H:%M:%S]") + ' ')


def _write_log(action):
    log = open('../log.txt', 'a')
    log.write(_get_current_time() + action + '\n')
    log.close()


@pytest.fixture
def write_log():
    return _write_log
