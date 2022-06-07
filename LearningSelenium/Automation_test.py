from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import fspath
import details
import pytest

class TestFibersafeDashboard():
    #exec_path = "C:\\Users\\User\\Downloads\\latest\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"

    @pytest.fixture(scope="session")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path=self.exec_path)
        driver.implicitly_wait(10)
        driver.get(self.base_URL)
        driver.maximize_window()
        yield
        print("Test Completed")
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        #self.driver.get('https://fibersafe.tmrnd.com.my:84/portal/login')
        #self.driver.get('https://patrol.tmrnd.com.my/portal/login')
        driver.find_element_by_id(fspath.Login.login_usrname).send_keys(details.tenantuser)
        driver.find_element_by_id(fspath.Login.login_pass).send_keys(details.tenantpass)
        driver.find_element_by_xpath(fspath.Login.login_button).click()
        time.sleep(30)

