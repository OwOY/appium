# -*- encoding=utf8 -*-
__author__ = "jingm"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import emoji
import string
import re
import os
from random import randint

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


class filters:

    def content_filter(content):
        
        content = emoji.demojize(content, delimiters=(':',':'))
        return content


    def title_filter(title):
        
        
        
        title = emoji.demojize(title, delimiters=(':',':'))
        title = re.sub('[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", title)
        title = re.sub(':\S+?:',' ',title)
        
        return title
    
   

def move_download_and_clean(title):
    
    for xhs_download in os.popen('adb shell "ls /storage/sdcard0/DCIM/Camera/*.mp4"').readlines():
        xhs_download = xhs_download.strip().split('/')[-1]
        
        try:
            os.system(f'adb pull /storage/sdcard0/DCIM/Camera/{xhs_download} C:/Users/jingm/Desktop/tiktok/download/{xhs_download}')
            os.rename(f'C:/Users/jingm/Desktop/tiktok/download/{xhs_download}', f'C:/Users/jingm/Desktop/tiktok/download/{title}.mp4')
        except:
            pass
        
    try:
        os.popen('adb shell "rm -r /storage/sdcard0/DCIM/Camera/*.mp4"')
    except:
        pass


    
    
    
    
    
    

    
def main():
    rest = randint(2, 5)
    poco(text="抖音").click()
    sleep(5)

    while True:
        try:
            try:
                title = poco(name = "com.ss.android.ugc.aweme:id/a94").get_text()
            except:
                title = poco(name = "com.ss.android.ugc.aweme:id/title").get_text()
            title = filters.title_filter(title)
            print(f'======================{title}==========================')
            #點擊分享按鈕
            poco("com.ss.android.ugc.aweme:id/g72").click()
            sleep(0.5)
            #點擊下載
            poco("android.widget.LinearLayout").offspring("com.ss.android.ugc.aweme:id/c3").child("android.widget.LinearLayout")[1].offspring("com.ss.android.ugc.aweme:id/g64").click()
            #確認是否下載完成
            while True:
                try:
                    poco(name = "com.ss.android.ugc.aweme:id/e7f").click()
                except:
                    break
            sleep(rest)
            move_download_and_clean(title)
        except:
            pass
        poco.swipe([0.5, 0.7], [0.5, 0.3], duration = 0.3)
        sleep(rest)

    
    
    
if __name__ == '__main__':
    
    main()



