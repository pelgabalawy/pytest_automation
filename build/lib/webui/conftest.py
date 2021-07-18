import pytest
from selenium import webdriver

# ------------------------------
# ----  command lines args -----
# ------------------------------
def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="",
        help="The landing page of the web application that you are testing")
    parser.addoption("--username", action="store", default="",
                     help="the username that will be used for auth")
    parser.addoption("--password", action="store", default="",
                     help="the password that will be used for auth")


def pytest_generate_tests(metafunc):
    url = metafunc.config.getoption("url")
    username = metafunc.config.getoption("username")
    password = metafunc.config.getoption("password")
    if url and hasattr(metafunc.cls, "url"):
        metafunc.cls.url = url
        metafunc.cls.username = username
        metafunc.cls.password = password


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# ----------------------
# ----  listeners ------
# ----------------------
@pytest.fixture(scope="class")
def test_suite_listener():
    # before the test suite
    print("before a test suite")

    yield

    # after the test suite
    print("after a test suite")


@pytest.fixture(scope="function")
def test_case_listener(request):
    # before test case
    request.cls.driver = webdriver.Chrome(executable_path="_drivers/linux/chromedriver")

    yield

    # after test case
    request.cls.driver.quit()