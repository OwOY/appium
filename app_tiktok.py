from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from mitmproxy import http
# from mitmproxy import HTTPFlow
from time import sleep
import requests

video_path = r'D:/video'





DRIVER_SERVER = r'http://127.0.0.1:4723/wd/hub'


# def response(flow: http.HTTPFlow):
#     req = flow.request
#     print(req.url)




desired_caps = {
  "platformName": "Android",
  "plathformVersion": "7.2.2",
  "deviceName": "test1018",
  "newCommandTimeout": "2000",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.main.MainActivity"
}

driver = webdriver.Remote(DRIVER_SERVER, desired_caps)
# wait = WebDriverWait(driver, 300)
sleep(5)


driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]').click()
sleep(2)
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
# sleep(2)
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]').click()
# sleep(2)
while True:
    driver.swipe(200, 1000, 200, 200)
    sleep(3)

# driver = webdriver.Remote(DRIVER_SERVER, desired_caps)