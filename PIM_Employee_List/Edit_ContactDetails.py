import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from element import elem
from Data import addData

class TestEditEmployee(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # variable data
        self.url = "https://opensource-demo.orangehrmlive.com"

    def tearDown(self):
        self.browser.quit()
        #edit Employee 
    def test_edit_contactdetails(self):
        #step
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuPIM).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.nameEmployee).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearchk).click()
        time.sleep(3)
        # Button Edit
        driver.find_element(By.XPATH,"//i[contains(@class,'oxd-icon bi-pencil-fill')]").click()
        time.sleep(5)
        # Button Edit Contact Detail
        driver.find_element(By.XPATH, elem.editContactDetails).click()
        time.sleep(3)

        # Edit Data
        streetEdit = driver.find_element(By.XPATH, elem.streetEdit)
        streetEdit.send_keys("JL. RANCA")
        time.sleep(2)
        cityEdit = driver.find_element(By.XPATH, elem.cityEdit)
        cityEdit.send_keys("Cilacap")
        time.sleep(2)
        stateEdit = driver.find_element(By.XPATH, elem.stateEdit)
        stateEdit.send_keys("Jawa Tengah")
        time.sleep(2)
        mobileEdit = driver.find_element(By.XPATH, elem.mobileEdit)
        mobileEdit.send_keys("0987654321")
        time.sleep(2)

                       
        #Save Data
        driver.find_element(By.XPATH, elem.saveContact).click()
        time.sleep(3)

        #validasi
        response_data = driver.find_element(
            By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn(response_data, 'Employee List')    


if __name__ == "__main__":
    unittest.main()