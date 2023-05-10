from selenium import webdriver

class WebDriverManager(object):

    __driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls.__driver is None:
            if (browser.lower()) == "chrome":
                
                # Please check the virtual environment path and provide your own virtual folder path that you have created

                cls.__driver =  webdriver.Chrome("C:/Users/ett21011/Desktop/ett_ta_2023/virtual/Scripts/chromedriver.exe")   

        return cls.__driver