from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
from mitmproxy import http
# from mitmproxy import HTTPFlow
from time import sleep
import requests
from appium.webdriver.common.touch_action import TouchAction
from txt import txt
from content_filter import filters
from random import randint
import os



def set_driver():
    
    DRIVER_SERVER = r'http://127.0.0.1:4723/wd/hub'


    desired_caps = {
    "platformName": "Android",
    "plathformVersion": "8.1.0",
    "deviceName": "HUAWEI Y7 Pro 2019",
    "newCommandTimeout": "2000",
    #   "appPackage": "com.xingin.xhs",
    #   "appActivity": "com.xingin.xhs.activity.SplashActivity",
    # "app":"D:/app/app/xiaohongshu.apk"
    }

    driver = webdriver.Remote(DRIVER_SERVER, desired_caps)
    # wait = WebDriverWait(driver, 300)
    sleep(5)
    return driver


def open_app(driver):

    driver.swipe(500, 500, 200, 500)   # 座標定位
    try:
        driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="第 2 個螢幕，共 2 個"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@text="小红书"]').click()
    except:
        pass
    sleep(5)

def login(driver):
    
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.TextView[@text="手机号登录"]').click()
    sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView').click()
    sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.FrameLayout[3]//*[@text="香港(中国)"]').click()
    sleep(3)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.EditText').send_keys('67074861')
    sleep(2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[@text="获取验证码"]').click()
    sleep(20)
    #check_pwd = get_mail()
    return driver

# def get_mail():

def get_article(driver):
    
    page = 1  
    while True:
        if page == 10:
            driver.swipe(200, 1000, 200, 200)    #座標定位
            page = 1
            
        try:
            element = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[{page}]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView[2]')        
        except:
            element = 0
            
        try:
            driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[{page}]').click()
        except:
            page += 1
            continue
        sleep(3)
        
            
        if element == 0: 
            get_normal_article(driver)
        else:
            get_video_article(driver)            

        try:
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.ImageView').click()
        except:
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]').click()
        page += 1
        
        sleep(5)
        
        
def get_normal_article(driver):      
    
    while True:
        try:
            element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ImageView')
            TouchAction(driver).long_press(element).perform()
            sleep(1)
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]').click()
            sleep(1)
        except:
            break
    
    try:
        title = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[1]').text
        title = filters.title_filter(title)
        print(f'================{title}=================')
    except:
        title = ''
    try:
        
        content = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]').text
        content = filters.content_filter(content)
        print(content)
    except:
        content = ''
    
    
    if title == '' and content == '':
        pass
    else:
        if not os.path.isfile(f'txt/{title}.txt'):
            txt.txt_write(title, content)
            
            
            
def get_video_article(driver):      
    
    try:
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.TextView').click()
    except:
        pass
    
    try:
        title = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.TextView').text
        title = filters.title_filter(title)
        print(f'================{title}=================')
    except:
        title = ''
  
    content = ''
    
    if title == '' and content == '':
        pass
    else:
        if not os.path.isfile(f'txt/{title}.txt'):
            txt.txt_write(title, content)

    
   
    
    
if __name__ == '__main__':
    
    driver = set_driver()
    open_app(driver)
    # login(driver)
    get_article(driver)
    
    