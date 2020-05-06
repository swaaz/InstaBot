#importing libraries and files
from selenium import webdriver
from time import sleep
import sys
import secrets
#getting values from secrets.py file and assigning the values to username and password
username = secrets.usr
password = secrets.pwd
#creating class to automate
class Instabot():
    def __init__(self,username,password):
        self.username = username    #storing the username in class
        self.password = password    #storig the password in class
        self.driver = webdriver.Firefox(executable_path = "./geckodriver-v0.26.0-linux64/geckodriver") #this is the path of webdriver, here I used geckodriver since I am using Firefox. Change the path of webdriver if you are not using Firefox
        self.driver.get("https://instagram.com/") 
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)    #entering the username 
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)    #entering the password
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()   #clicking on login button
        sleep(6)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  #clicking on 'Not Now' option
        sleep(4)

    def get_pending_request(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type = 'button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Privacy and Security')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'View Account Data')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a").click()
        sleep(2)
        while True:
            try:
                pending_id = self._getnames()
                print(pending_id)
                sleep(2)
                self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(pending_id)
                sleep(3)
                self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(pending_id)).click()
                sleep(2)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Requested')]").click()
                sleep(3)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                sleep(3)
                self.driver.back()
                sleep(3)
                self.driver.refresh()
                sleep(3)
            except:
                print("Tadaaaa!!!!!")
                sys.exit()
        

    def _getnames(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main")
        links = scroll_box.find_element_by_class_name("-utLf").text
        return links
        


bot = Instabot(username,password)
bot.get_pending_request()

