#importing libraries and files
from selenium import webdriver
from time import sleep
import sys
import secrets

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


#getting values usr and pwd from secrets.py file and assigning the values to username and password
username = secrets.usr
password = secrets.pwd

#creating class to automate
class Instabot():

    #function to login
    def __init__(self,username,password):
        self.username = username    #storing the username in class
        self.password = password    #storig the password in class
        self.driver = webdriver.Firefox(executable_path = "./webdrivers/firefox_webdriver/geckodriver-v0.26.0-linux64/geckodriver") #this is the path of webdriver, here I used geckodriver-linux since I am using Firefox in linux. Change the path of webdriver according to your environment
        self.driver.get("https://instagram.com/")
        self._make_driver_wait("//input[@name=\"username\"]")
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)    
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)    
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        self._make_driver_wait("//button[contains(text(), 'Not Now')]")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        self._make_driver_wait("//button[contains(text(), 'Not Now')]")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)

    #function to cancel all the pending follow requests
    def cancel_sent_requests(self):
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        self._make_driver_wait("//div[@class = 'AFWDX']")
        self.driver.find_element_by_xpath("//button[@type = 'button']").click()
        self._make_driver_wait("//a[contains(text(), 'Privacy and Security')]")
        self.driver.find_element_by_xpath("//a[contains(text(), 'Privacy and Security')]").click()
        self._make_driver_wait("//a[contains(text(), 'View Account Data')]")
        self.driver.find_element_by_xpath("//a[contains(text(), 'View Account Data')]").click()
        self._make_driver_wait("/html/body/div[1]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main/div/div[2]/section[1]/section[1]/a").click()
        sleep(2)
        print("\n****** Cancelling Requests ******\n")
        z = True
        prev = " "
        count = 0
        while z:
            try:
                pending_id = self._get_pending_names()
                if pending_id != prev:
                    count += 1
                    print(count,pending_id)
                    prev = pending_id
                self._make_driver_wait("//input[@placeholder=\"Search\"]")
                self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(pending_id)
                self._make_driver_wait("//a[contains(@href,'/{}/')]".format(pending_id))
                self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(pending_id)).click()
                self._make_driver_wait("//button[contains(text(), 'Requested')]")
                self.driver.find_element_by_xpath("//button[contains(text(), 'Requested')]").click()
                self._make_driver_wait("//button[contains(text(), 'Unfollow')]")
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                sleep(2)
                self.driver.back()
                sleep(3)
                self.driver.refresh()
            except:
                print("Tadaaaa!!!!!, Task Completed!!!!")
                z = False
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()

    #function which return the name from the list
    def _get_pending_names(self):
        self._make_driver_wait("/html/body/div[1]/section/main/div/article/main")
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main")
        self._make_driver_wait("-utLf", "class_name")
        links = scroll_box.find_element_by_class_name("-utLf").text
        return links

    #function to get the names of unfollowers
    def get_unfollowers(self):
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        self._make_driver_wait("//a[contains(@href,'/following')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self._make_driver_wait("//a[contains(@href,'/followers')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print("\n****** Unfollowers ******\n")
        prev = " "
        count = 0
        for x in not_following_back :
            if prev != x:
                count += 1
                print(count,x)
                prev = x
        
    #function to get the names of fans
    def get_fans(self):
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        self._make_driver_wait("//a[contains(@href,'/following')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self._make_driver_wait("//a[contains(@href,'/followers')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        fans = [user for user in followers if user not in following]
        print("\n****** Fans ******\n")
        prev = " "
        count = 0
        for x in fans :
            if prev != x:
                count += 1
                print(count,x)
                prev = x

    #function which returns list of names
    def _get_names(self):
        self._make_driver_wait("/html/body/div[4]/div/div[2]")
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;", scroll_box)
        self._make_driver_wait('a', "tag_name")
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self._make_driver_wait("/html/body/div[4]/div/div[1]/div/div[2]/button")
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names
    
    #function cancel unfollowers
    def cancel_unfollowers(self):
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        self._make_driver_wait("//a[contains(@href,'/following')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self._make_driver_wait("//a[contains(@href,'/followers')]")
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        for x in not_following_back:
            y = None
            self._make_driver_wait("//input[@placeholder='Search']")
            print('found')
            self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(x)
            print('Search for {}'.format(x))
            self._make_driver_wait("//a[contains(@href,'/{}/')]".format(x))
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(x)).click()
            print("\nDo you want to unfollow : {}".format(x))
            y = input("1. Yes\t2. No\nEnter the choice : ")
            if y == "1":
                self._make_driver_wait("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button")
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button").click()
                self._make_driver_wait("//button[contains(text(), 'Unfollow')]")
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
            else:
                continue

    def Exit(self):
        self._make_driver_wait("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        self._make_driver_wait("/html/body/div[1]/section/main/div/header/section/div[1]/div/button")
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
        self._make_driver_wait("//button[contains(text(), 'Log Out')]")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log Out')]").click()

    def _make_driver_wait(self, element_to_locate, by='xpath'):
        wait = WebDriverWait(self.driver, 20)
        if by == 'xpath':
            wait.until(EC.element_to_be_clickable((By.XPATH, element_to_locate)))
        elif by == 'class_name':
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, element_to_locate)))
        elif by == 'tag_name':
            wait.until(EC.element_to_be_clickable((By.TAG_NAME, element_to_locate)))


#main function
def main():
    bot = Instabot(username,password)
    a = True
    while a:
        print()
        print("****** Insta-Bot ******")
        x = input("1. list Un-followers\n2. list Fans\n3. Cancel all the sent follow requests\n4. Unfollowers those who don't follow you back\n5. Exit\nEnter the choice : ")
        if x == "1":
            bot.get_unfollowers()
        elif x == "2":
            bot.get_fans()
        elif x == "3":
            bot.cancel_sent_requests()
        elif x == "4":
            bot.cancel_unfollowers()
        elif x == "5":
            bot.Exit()
            a = False
        else:
            print("Invalid option!!")
        

main()