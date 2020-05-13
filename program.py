#importing libraries and files
from selenium import webdriver
from time import sleep
import sys
import secrets

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
        sleep(6)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)    
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)    
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()   
        sleep(6)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()  
        sleep(4)

    #function to cancel all the pending follow requests
    def cancel_sent_requests(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type = 'button']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Privacy and Security')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'View Account Data')]").click()
        sleep(2)
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
                sleep(3)
                self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(pending_id)
                sleep(4)
                self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(pending_id)).click()
                sleep(4)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Requested')]").click()
                sleep(4)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                sleep(4)
                self.driver.back()
                sleep(4)
                self.driver.refresh()
                sleep(4)
            except:
                print("Tadaaaa!!!!!, Task Completed!!!!")
                z = False
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()

    #function which return the name from the list
    def _get_pending_names(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/main")
        links = scroll_box.find_element_by_class_name("-utLf").text
        return links

    #function to get the names of unfollowers
    def get_unfollowers(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
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
        sleep(4)
        
        
    #function to get the names of fans
    def get_fans(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
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
        sleep(4)

    #function which returns list of names
    def _get_names(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;", scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names


#main function
def main():
    bot = Instabot(username,password)
    a = True
    while a:
        print()
        print("****** Insta-Bot ******")
        x = input("1. list Un-followers\n2. list Fans\n3. Cancel all the sent follow requests\n4. Exit\nEnter the choice : ")
        if x == "1":
            bot.get_unfollowers()
        elif x == "2":
            bot.get_fans()
        elif x == "3":
            bot.cancel_sent_requests()
        elif x == "4":
            a = False
        else:
            print("Invalid option!!")
        

main()