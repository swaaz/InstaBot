<h1 align="center"> InstaBot</h1>
<h2 align="center"> Bot built for Instagram using Python and Selenium. </h2>
<h3 align="center"> This is a simple Instagram bot that cancels all the follow requests which you have sent before. This Bot makes sure that all the following request which you have sent will be canceled and save your account from Blocking because the total number of the following request you sent crosses 200, then your account will be blocked and you cannot send follow request anymore.</h3>
<div align="center">
<img src="./src/bot.gif" width="300x" height="400px">
</div>

### Clone project
first you need to fork and then copy the url from clone option
```
$ git clone [url]
```
### Install Python 3
```
$ sudo apt-get update
$ sudo apt-get install python3.7
```
### Install Selenium
```
$ pip3 install selenium
```
### Change the webdriver path
#### the path of the webdriver has to changed according to your environment
edit the 18ₜₕ line of file  ``` ./program.py ```
```
self.driver = webdriver.Firefox(executable_path = "[path]")
```
example:
```
self.driver = webdriver.Firefox(executable_path = "./webdrivers/firefox_webdriver/geckodriver-v0.26.0-linux64/geckodriver")
```
#### file structure:
```
.
├── webdriver
│   ├── chrome_webdriver
│   │   ├── Chrome_webdriver_linux64
│   │   ├── Chrome_webdriver_mac64
│   │   ├── Chrome_webdriver_win32
|   |
|   ├── firefox_webdriver
|   |   ├── geckodriver-v0.26.0-linux64
│   │   ├── geckodriver-v0.26.0-macos
│   │   ├── geckodriver-v0.26.0-win32
```
### Add username and password
edit the ```./secrets.py``` file and add your username and passport
```
usr = "[username]" 
pwd = "[password]"
```
### Run the program
```
$ pip3 program.py
```