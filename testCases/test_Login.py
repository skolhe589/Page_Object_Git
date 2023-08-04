from pageObjects.LoginPage import Login


class Test_CredKart_Login:

    # def test_pageTitle_001(self, setup):
    #     self.driver = setup
    #     if self.driver.title == "CredKart":
    #         self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_pass.PNG")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\ScreenSHots\\test_pageTitle_001_fail.PNG")
    #         self.driver.close()
    #         assert False

    def test_CredKart_Login_002(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Click_Login_link()
        #self.driver.get("https://automation.credence.in/login")
        self.lp.Enter_Email("Credencetest@test.com")
        # self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")
        self.lp.CLick_Login_Button()
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print(self.lp.Login_Status())
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
            assert False

        # try:
        #     self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
        #     print("Login TestCase is Passed")
        #     self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
        #     self.driver.close()
        #
        #     assert True
        # except:
        #     print("Login TestCase is Failed")
        #     self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
        #     self.driver.close()
        #     assert False

# 100s testcases--> if you have to run it in firefox

# pytest -v --html=Reports/myreport.html --alluredir="AllureReports" -n=2  testCases/test_Login.py --browser chrome
