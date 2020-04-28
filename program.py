from selenium import webdriver
from time import sleep

class Instabot():
    def __init__(self,username,password):
        self.driver = webdriver.Firefox(executable_path = "/home/swaaz/swaaz/InstaBot/geckodriver-v0.26.0-linux64/geckodriver")
        self.driver.get("https://instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), '_swaaz_' )]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type = 'button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[7]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'View Account Data')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a").click()
        
    
bot = Instabot()
