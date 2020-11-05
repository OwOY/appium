# -*- encoding=utf8 -*-
__author__ = "jingm"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from random import randint
from random import uniform
import os
import codecs

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)


def find_utube():
    
    while True:
        times = 0
        if poco(text = 'YouTube').exists():
            poco(text = "YouTube").click()
            break
        elif times == 5:
            print('找不到Youtube')
            break
        else:
            poco.swipe([0.8, 0.5], [0.3, 0.5], duration = 0.3)

        times += 1

def push_video_in_mobile(path):
    for video in os.listdir(path):
        os.system(f'adb push {path}/{video} /storage/sdcard0/DCIM/Camera/Video/{video}')
        os.system(f'adb shell "am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///storage/sdcard0/DCIM/Camera/Video/{video}"')


def post_video():
    
    mount = 1
    number = 0
    repeat_title = ''
    repeat_times = 0
    sleep(3)
    
    while True:
        rest = randint(3,7)
        try:
            poco(desc = "影片").click()
        except:
            pass
        title = poco("com.google.android.youtube:id/media_grid_recycler_view").child("android.widget.FrameLayout")[number].child("com.google.android.youtube:id/thumb_image_view_parent").child("com.google.android.youtube:id/thumb_image_view").attr('desc')
        title = title.replace('.mp4','')
        txt.check_post_list_txt()
        
        if title not in txt.check_post_list(title):
            sleep(rest)
            txt.write_post_OK(title)
            poco("com.google.android.youtube:id/media_grid_recycler_view").child("android.widget.FrameLayout")[number].click()
            set_video_info(title)
            os.system(f'adb shell "rm /storage/sdcard0/DCIM/Camera/Video/{title}.mp4"')   #上傳後即刪除
            print(f'第{mount}支影片 : {title} 上傳成功')
            mount += 1
            
        else:
            print(f'{title} 影片已上傳過')
            number += 1
            if repeat_title == title:
                repeat_times += 1
                if repeat_times > 5:
                    print('重覆過多')
                    break
                
            repeat_title = title
            if number == 12:
                number = 0
                poco.swipe([0.5, 0.7], [0.5, 0.3], duration = 0.3)

#為了避免重複上傳   建置post_OK.txt            
class txt:
    
    
    def check_post_list_txt():
        if not os.path.isfile('post_OK.txt'):
            with codecs.open('post_OK.txt','w','utf-8')as f:
                f.write('')
    def write_post_OK(title):
        with codecs.open('post_OK.txt','a','utf-8')as f:
            f.write(f'{title}\n')

    def check_post_list(title):
        with codecs.open('post_OK.txt','r','utf-8')as f:
            post_OK_list = f.readlines()
        post_OK_list = [post_OK.strip() for post_OK in post_OK_list]
        return post_OK_list


def set_video_info(title):
    rest = randint(0, 2)
    key_in = randint(5, 13)
    swipe_speed = uniform(0.3, 1.2)
    post_rest = uniform(10.0, 19.0)
    sleep(rest)
    poco.swipe([0.5, 0.9], [0.5, 0.3], duration = swipe_speed)
    sleep(key_in)
    poco("com.google.android.youtube:id/title_edit").set_text(title)
    sleep(rest)
    poco(desc="上傳").click()
    sleep(post_rest)
    
    
    
    
    
    
    
    
    
def main():
    path = input('請輸入影片放置路徑(ex:E:/Video) :')
    push_video_in_mobile(path)
    find_utube()
    post_video()



if __name__ == '__main__':
    main()
