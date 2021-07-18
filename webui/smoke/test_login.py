# internal imports
import pytest

# pages imported to be used in the test
from webui.pages.page_login import Login_page

# command example: pytest ./webui/smoke --url=https://www.google.com --username=pelgabalawy@gmail.com
# --password=1234! --json=./reports/webui_smoke.json


# this is a test suite
@pytest.mark.usefixtures("test_suite_listener")
class Test_login_suite:
    url, username, password = None, None, None

    # this is a test case
    @pytest.mark.usefixtures("test_case_listener")
    def test_login(self):
        pglogin = Login_page(self.driver)
        pglogin.login(url=self.url,
                      username=self.username,
                      password=self.password)
