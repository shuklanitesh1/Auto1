import time

import selenium


def auto_search(self):
    print(" The Page Title is : ", self.driver.title)
    self.driver.maximize_window()
    time.sleep(2)
    self.do_click(self.Accept_Cookies)
    time.sleep(2)
    self.do_click(self.Brand_Model)
    print("click Operation happened on Brand and Model Tab")
    time.sleep(2)
    # self.driver.get('https://www.autohero.com/de/search/?brand=VOLKSWAGEN&model=VOLKSWAGEN.Golf&mileageMax=25000')
    self.do_click(self.Volkswagen)
    print("Volkswagen Car Brand is selected now. ")
    time.sleep(3)
    # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='golf']")))
    # ActionChains(driver).move_to_element(element).click().perform()
    self.do_click(self.Golf)
    print("Golf Model for Volkswagen Car is selected now. ")
    time.sleep(3)
    self.do_click(self.Basic_Filter)
    time.sleep(3)
    self.do_click(self.KM)
    print("The Max Value of Kms driven selected is : 25.000 km")
    time.sleep(3)