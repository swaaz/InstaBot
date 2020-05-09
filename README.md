<h1 align="center"> InstaBot</h1>
<h2 align="center"> Bot built for Instagram using Python and Selenium. </h2>
<h3 align="center"> 
This is an Instagram bot that can automate and perform some tasks; makes your task easier. This Bot can show the list of un-followers from you Instagram or it can show your fans and also it can cancel all the pending follow requests which you have sent before.
</h3>
<div align="center">
    <img src="./src/bot.gif" width="300x" height="400px">
</div>

### Clone project
first you need to fork and then copy the url from clone option  
run in gitbash or terminal :
```
$ git clone [url]
```
### Install Python 3
run in terminal :
```
$ sudo apt-get update
$ sudo apt-get install python3.7
```
### Install PIP
#### For Windows user
- Download the ```git-pip.py``` by clicking [here](https://bootstrap.pypa.io/get-pip.py)
- run in gitbash or cmd :
```
$ python get-pip.py
```
- verify by running :
```
$ pip -V
```
#### For linux user
- run in terminal :
```
$ apt install python3-pip
or
$ python get-pip.py     
```
### Install Selenium
run in terminal or cmd/gitbash
```
$ pip install selenium
or
$ pip3 install selenium
```
### Change the webdriver path
The path of the webdriver has to changed according to your environment
edit the 18ₜₕ line of file  ``` ./program.py ```
#### linux user
##### if you are using firefox
```
self.driver = webdriver.Firefox(executable_path = "./webdrivers/firefox_webdriver/geckodriver-v0.26.0-linux64/geckodriver")
```
##### if you are using chrome

```
self.driver = webdriver.Chrome(executable_path = "./webdrivers/chrome_webdriver/chromedriver_linux64/chromedriver")
```
#### Windows user
<strong> Read the Instruction carefully </strong>

##### if you are using firefox
<strong>copy the path of webdriver depending upon your environment and add the path to Environment Variable as isntructed below</strong>

example path
```
C:\Users\swaaz\Downloads\temp\InstaBot\webdrivers\firefox_webdriver\geckodriver-v0.26.0-win32\
```

copy the code and paste in 18ₜₕ line
```
self.driver = webdriver.Firefox(executable_path = ".\\webdrivers\\firefox_webdriver\\geckodriver-v0.26.0-win32\\geckodriver.exe")
```

##### if you are using chrome
<strong>copy the path of webdriver depending upon your environment and add the path to Environment Variable as isntructed below</strong>

example
```
C:\Users\swaaz\Downloads\temp\InstaBot\webdrivers\chrome_webdriver\chromedriver_win32\
```

<strong>Read the instruction given below carefully</strong>
copy the code and paste in 18ₜₕ line

```
self.driver = webdriver.Chrome(executable_path = ".\\webdrivers\\chrome_webdrive\\chromedriver_win32\\geckodriver.exe")
```
#### Instructions to add path to your Environment variable
- Copy the path of the webdriver
- follow the instruction given below
<div align="center">
    <div><img src="./src/1.png" width="70%"><div>
    <div><img src="./src/2.png"width="70%"><div>
    <div><img src="./src/3.png"width="70%"><div>
    <div><img src="./src/4.png"width="70%"><div>
    <div><img src="./src/5.png"width="70%"><div>
    <div><img src="./src/6.png"width="70%"><div>
</div>  
<div align="left">

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
$ python program.py
or
$ python3 program.py
```
### Helpful links
- [Installing PIP on Windows](https://www.liquidweb.com/kb/install-pip-windows/)
- [Installing PIP in Linux](https://www.tecmint.com/install-pip-in-linux/)
- [Download Geckodriver](https://github.com/mozilla/geckodriver/releases)
- [Download Chrome Driver](https://chromedriver.chromium.org/downloads)
- [Setup selenium and webdriver for Linux](https://www.youtube.com/watch?v=CriSHYMtg9M)
- [Setup selenium and webdriver for Windows](https://youtu.be/FFDDN1C1MEQ)
