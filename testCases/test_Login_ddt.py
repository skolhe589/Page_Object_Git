from pageObjects.LoginPage import Login
from utilities import XLutils


class Test_CredKart_Login_DTT:
    XlPath = "D:\\SHUBH\\IT Software\\Python\\CredKart_Pytest_Project _TusharSir\\testCases\\TestData\\LoginTest - Copy.xlsx"

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

    def test_CredKart_Login_ddt_006(self, setup):
        self.driver = setup  # open browser
        self.lp = Login(self.driver)  # pageobject call
        self.row = XLutils.RowCount(self.XlPath, "Sheet1")  # xl row count
        print("Number of rows in excel is " + str(self.row))
        Login_status_List = []
        for r in range(2, self.row + 1):  # iterate xl rows
            self.email = XLutils.ReadData(self.XlPath, "Sheet1", r, 2)  # email read
            self.password = XLutils.ReadData(self.XlPath, "Sheet1", r, 3)  # password read
            self.exp_result = XLutils.ReadData(self.XlPath, "Sheet1", r, 4)  # exp result read
            self.lp.Click_Login_link()
            self.lp.Enter_Email(self.email)
            self.lp.Enter_Password(self.password)
            self.lp.CLick_Login_Button()
            # print(self.lp.Login_Status())
            if self.lp.Login_Status() == True:
                if self.exp_result == "Pass":
                    Login_status_List.append("Pass")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
                    self.lp.CLick_Menu_Button()
                    self.lp.CLick_Logout_Button()
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Pass")
                elif self.exp_result == "Fail":
                    Login_status_List.append("Fail")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_pass.PNG")
                    self.lp.CLick_Menu_Button()
                    self.lp.CLick_Logout_Button()
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Fail")
            if self.lp.Login_Status() == False:
                if self.exp_result == "Pass":
                    Login_status_List.append("Fail")
                    self.driver.save_screenshot(".\\ScreenSHots\\test_CredKart_Login_002_fail.PNG")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Fail")
                elif self.exp_result == "Fail":
                    Login_status_List.append("Pass")
                    XLutils.WriteData(self.XlPath, "Sheet1", r, 5, "Pass")
        print(Login_status_List)
        if "Fail" not in Login_status_List:
            assert True
        else:
            assert False

# 100s testcases--> if you have to run it in firefox

# pytest -v --html=Reports/myreport.html --alluredir="AllureReports" -n=2  testCases/test_Login.py --browser chrome
