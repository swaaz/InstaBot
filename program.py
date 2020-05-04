from selenium import webdriver
from time import sleep
import secrets
password = secrets.pwd
names = []
class Instabot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path = "/home/swaaz/swaaz/InstaBot/geckodriver-v0.26.0-linux64/geckodriver")
        self.driver.get("https://instagram.com/")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(6)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(2)
    def get_pending_request(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type = 'button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[7]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'View Account Data')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a").click()
        sleep(2)
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

    def _getnames(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main")
        links = scroll_box.find_element_by_class_name("-utLf").text
        return links
        
    

bot = Instabot('_swaaz_',password)
bot.get_pending_request()

