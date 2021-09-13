from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage

import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#import pyrobot
import keyboard


class StartPage(BasePage):
    Brand_Model = (By.XPATH, "//span[contains(text(),'Marke & Modell')]")
    Accept_Cookies = (By.XPATH, "//button[contains(text(),'Alles akzeptieren')]")
    Top_Models = (By.CSS_SELECTOR,
                  "div.layout___1ETzW div.container___27E1u.container___1Rv1r div.filterSectionWrapper___SrkFt div.root___1yEZq div.filters___1lGDM div.root___1GlEV:nth-child(2) div.container___2SMPk.container___2FB5N.containerBottomStart___FqLOJ > div:nth-child(1)")
    Volkswagen = (By.XPATH, "//input[@value='Volkswagen'][1]")
    Golf = (By.XPATH,
            "//div[@class='container___2SMPk container___AV3J0 containerBottomStart___FqLOJ']/ul/li[6]/input[@value='Golf']")
    KM = (By.XPATH, "//select[@data-qa-selector='select-mileage-to']//option[@value='2']")
    Basic_Filter = (By.XPATH, "//button[@id='basicFilter']")
    Brand_name = (By.XPATH, "//div[@role='rowgroup']//div/a/div[2]/div/h2")

    #total_brands = (By.XPATH,"//div[@class='root___1FrTY']//div[@role='grid']/div/div")
    # html = (By.TAG_NAME, "html");

    """Constructor Of the Page Class"""

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(Testdata.BASE_URL)
        self.driver.get('https://www.autohero.com/de/search/')

    """Page Actions for Start Page """

    """This is used to get the title of the Page"""

    def get_title_start_page(self, title):
        print(self.get_title(title))
        return self.get_title(title)

    def click_mark_model(self):
        self.do_click(self.Brand_Model)
        print("click happened")
        time.sleep(3)

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

    def brand_model_verification(self):
        print("Brand and model verifications starts")
        self.driver.get("https://www.autohero.com/de/search/?brand=VOLKSWAGEN&model=VOLKSWAGEN.Golf&mileageMax=25000")
        time.sleep(5)
        # self.driver.execute_script("$('#values').css('zoom', 5);")
        # self.driver.execute_script("document.body.style.zoom='37%'")
        # time.sleep(20)

        for i in range(0, 7):
            keyboard.press_and_release('ctrl+-')
        time.sleep(3)
        CarsListXpath = "//div[@class='root___1FrTY']//div[@role='rowgroup']/div"
        total_brands = self.driver.find_elements_by_xpath("//div[@class='root___1FrTY']//div[@role='rowgroup']/div")

        print(type(total_brands))
        print(total_brands)
        print(len(total_brands))
        time.sleep(3)

        for i in range(1, len(total_brands)-2):
            CarNameXpath = CarsListXpath + str([i]) + "//h2"
            #print(CarNameXpath)
            CarName = self.driver.find_element_by_xpath(CarNameXpath).text
            time.sleep(2)
            #print(CarName)
            if "Volkswagen Golf" in CarName:
                print(CarName)
                KilometerXpath = CarsListXpath + str([i]) + "//ul/li[3]"
                Kilometer = self.driver.find_element_by_xpath(KilometerXpath).text
                #print(Kilometer)
                parameters = Kilometer.split("\n")
                #print(parameters)
                fetchkm = parameters[1].split(" ")
                #print(fetchkm)
                actualKm = fetchkm[0]
                print(actualKm)
                ExpectedKMvalue = 25.000
                if ExpectedKMvalue == actualKm:
                    print(CarName + " travelled " + str(actualKm) + " kms which is less than " + str(ExpectedKMvalue) + " Kms")
                else:
                    print(CarName + " travelled " + str(actualKm) + " kms which is less than " + str(ExpectedKMvalue) + " Kms")

                time.sleep(3)
            else:
                print(str(i) + "th Element does not have Volkswagen Golf ")
                #print(CarName)
        #for i in range(0, 7):
            #keyboard.press('ctrl+')
        time.sleep(3)
                #KilometerValue = float(actualKm)









            #print("Total List count is ", len(List_total_brands))


        #print("Total count is ", total_brands.count())
        """
        for i in range(0, 7):
            keyboard.press('ctrl')
            keyboard.press('+')
            keyboard.release('ctrl')
            keyboard.release('+')
        time.sleep(10)
        """


"""      
        selects = Select(self.KM)
        #selects.select_by_value('2')
        Select(driver.find_element_by_tag_name("selects")).select_by_value('2')
        #selects.select_by_visible_text('25.000 km')
        #select = Select(driver.find_element_by_id('fruits01'))
"""
