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
import shutil
from download import move_download_and_clean
from download import pic_download_and_clean

class swipe:
    
    
    def getSize(driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    def swipLeft(driver):
        l=swipe.getSize(driver)
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.3)
        x2=int(l[0]*0.05)
        driver.swipe(x1,y1,x2,y1)

    def swipDown(driver):
        l=swipe.getSize(driver)
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.8)
        y2=int(l[0]*0.2)
        driver.swipe(x1,y1,x1,y2)


    def swipRight(driver):
        l=swipe.getSize(driver)
        x1=int(l[0]*0.75)
        y1=int(l[1]*0.3)
        x2=int(l[0]*0.05)
        driver.swipe(x2,y1,x1,y1)


def set_driver():
    
    DRIVER_SERVER = r'http://127.0.0.1:4723/wd/hub'


    desired_caps = {
    "platformName": "Android",
    "plathformVersion": "8.2.0",
    "deviceName": "HUAWEI Y7 Pro 2019",
    "newCommandTimeout": "2000",
    #   "appPackage": "com.xingin.xhs",
    #   "appActivity": "com.xingin.xhs.activity.SplashActivity",
    # "app":"D:/app/app/xiaohongshu.apk"
    }

    driver = webdriver.Remote(DRIVER_SERVER, desired_caps)
    driver.implicitly_wait(5)
    # wait = WebDriverWait(driver, 300)
    return driver




def open_app(driver):
    
    swipe.swipLeft(driver)
    try:
        driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="第 2 個螢幕，共 2 個"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@text="小红书"]').click()
    except:
        pass
    # sleep(5)



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
            swipe.swipDown(driver)
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
        # sleep(3)
        
            
        if element == 0: 
            get_normal_article(driver)
        else:
            get_video_article(driver)            

        try:
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.ImageView').click()
        except:
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]').click()
        page += 1
        
        # sleep(5)
        
        
def get_normal_article(driver):      
    
    
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
        
        if not os.path.isdir(f'txt/{title}'):
            os.makedirs(f'txt/{title}')
        
        txt.txt_write(title, content)
            
        swipe.swipRight(driver)
        
        number = driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView').text
        pic_id = number.split('/')[0]
        pic_id = int(pic_id)
        
        total_pic = number.split('/')[-1]
        
        while pic_id <= int(total_pic):
            
            try:
                element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ImageView')
                TouchAction(driver).long_press(element).perform()
                sleep(1)
                driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]').click()
                try:
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[@text="允許"]').click()
                    sleep(2)
                except:
                    pass
                sleep(1)
                
                swipe.swipLeft(driver)
                sleep(0.5)
            except:
                break
            pic_id += 1
            
        pic_download_and_clean(title)
    sleep(3)
            
            
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
        if not os.path.isdir(f'txt/{title}'):
            os.makedirs(f'txt/{title}')
            
            txt.txt_write(title, content)
            
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]').click()
            sleep(2)
            driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView').click()
            sleep(2)
            
            while True:
                try: 
                    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
                    sleep(3)
                except:
                    break
                
            move_download_and_clean(title)
    sleep(3)
    
if __name__ == '__main__':
    
    
    driver = set_driver()
    open_app(driver)
    # # login(driver)
    get_article(driver)
    # get_normal_article(driver)
    
    