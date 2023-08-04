from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CredKart_CheckOut:
    Click_Product_MacBook_XPATH = (By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3")
    Click_AddToCart_XPATH = (By.XPATH, "//input[@value='Add to Cart']")
    Click_ProceedToCheckOut_XPATH = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    Enter_First_Name_XPATH = (By.XPATH, "//input[@id='first_name']")
    Enter_Last_Name_XPATH = (By.XPATH, "//input[@id='last_name']")
    Enter_Phone_XAPTH = (By.XPATH, "//input[@id='phone']")
    Enter_Address_XAPTH = (By.XPATH, "//textarea[@id='address']")
    Enter_Zip_XPATH = (By.XPATH, "//input[@id='zip']")
    DropDown_State_XPATH = (By.XPATH, "//select[@id='state']")
    Enter_Owner_Name_XPATH = (By.XPATH, "//input[@id='owner']")
    Enter_CVV_XPATH = (By.XPATH, "//input[@id='cvv']")
    DropDown_Year_XPATH = (By.XPATH, "//select[@id='exp_year']")
    DropDown_Month_XPATH = (By.XPATH, "//select[@id='exp_month']")
    Enter_Card_Number_XPATH = (By.XPATH, "//input[@id='cardNumber']")
    Click_Checkout_XPATH = (By.XPATH, "//button[@id='confirm-purchase']")
    Success_Message = (By.XPATH, "/html/body/div/div[1]/p[1]")

    def __init__(self, driver):
        self.driver = driver

    def Click_MacBook(self):
        self.driver.find_element(*CredKart_CheckOut.Click_Product_MacBook_XPATH).click()

    def DropDown_State(self, statename):
        state = Select(self.driver.find_element(*CredKart_CheckOut.DropDown_State_XPATH))
        state.select_by_visible_text(statename)
