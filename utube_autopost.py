# -*- encoding=utf8 -*-
__author__ = "jingm"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from random import randint
from random import uniform
import os
import codecs
import pymongo
import datetime
import shutil

nox_port = input('請輸入 Nox_Port : ')
connect_device(f'Android://127.0.0.1:5037/127.0.0.1:{nox_port}?cap_method=JAVACAP^&^&ori_method=ADBORI')
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# auto_setup(__file__, devices = [f'Android://127.0.0.1:5037/127.0.0.1:{nox_port}?cap_method=JAVACAP^&^&ori_method=ADBORI'])

client = pymongo.MongoClient('192.168.1.141:27017')
collection = client['youtube_post_OK']['video']

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
    for video_dir in os.listdir(path):
        for video in os.listdir(f'{path}{video_dir}'):
            if '.mp4' in video:
                os.system(f'adb -s 127.0.0.1:{nox_port} push {path}/{video_dir}/{video} /sdcard/DCIM/Camera/Video/{video}')
                os.system(f'adb -s 127.0.0.1:{nox_port} shell "am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/Video/{video}"')


def post_video(path):
    
    mount = 1
    number = 0
    repeat_title = ''
    repeat_times = 0
    sleep(10)
    
    while True:
        rest = randint(3,7)
        try:
            poco(name = "建立").click()
            sleep(1)
            poco("上傳影片").click()
            sleep(rest)
        except:
            pass
        
        title = poco("com.google.android.youtube:id/media_grid_recycler_view").child("android.widget.FrameLayout")[number].child("com.google.android.youtube:id/thumb_image_view_parent").child("com.google.android.youtube:id/thumb_image_view").attr('desc')
        title = title.replace('.mp4','')
#         txt.check_post_list_txt()
        mongo_data = collection.find({})
        get_mongo_title_list = []
        for data in mongo_data:
            get_mongo_title_list.append(data['title'])
            
#         if title not in txt.check_post_list(title):
#             sleep(rest)
#             txt.write_post_OK(title)
        if title not in get_mongo_title_list: 
            poco("com.google.android.youtube:id/media_grid_recycler_view").child("android.widget.FrameLayout")[number].click()
            set_video_info(path, title)
            youtube_url = get_youtube_url()
            print(f'第{mount}支影片 : {title} 上傳成功')
            
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S") 
            collection.insert_one({'url': youtube_url,\
            'title':title,\
            'time':f"{datetime.date.today()}_{current_time}"})
            mount += 1
            
        else:
            print(f'{title} 影片已上傳過')
            poco('向上瀏覽').click()
            sleep(1)
            
        os.system(f'adb -s 127.0.0.1:{nox_port} shell "rm /sdcard/DCIM/Camera/Video/{title}.mp4"')
        os.system(f'adb -s 127.0.0.1:{nox_port} shell "am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard"')
        shutil.rmtree(f'{path}{title}')
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


def set_video_info(path, title):
    rest = randint(1, 2)
    key_in = randint(3, 8)
    post_rest = uniform(15.0, 18.0)
    sleep(key_in)
    poco("android.widget.EditText").set_text(title)
    sleep(rest)
    
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.google.android.youtube:id/elements_fragment").child("android.view.View").child("android.view.View")[1].click() 
    
    dir_file = os.listdir(f'{path}{title}')
    for file_ in dir_file:
        if '.txt' in file_:
            txt_name = file_
    with codecs.open(f'{path}{title}\{txt_name}', 'r', 'utf-8')as f:
        content = f.read()
    print(content[0:5000])
    sleep(1)
    poco(text = "新增說明").set_text(content[0:5000])
    sleep(rest)
    poco(name = "返回。按鈕。").click()
    sleep(rest)
    poco(text="下一步").click()
    sleep(rest)
    poco(name="上傳").click()
    sleep(post_rest)
    while True:
        if not poco(text="可以觀看").exists():
            print('處理中...')
            
            sleep(10)
        else:
            poco.swipe([0.5, 0.2], [0.5,0.8] , duration = 0.5)
            sleep(3)
            break
            
def get_youtube_url():
    
    poco(name = "動作選單")[0].click()
    sleep(1)
    poco(text = "分享").click()    
    sleep(1)
    poco(text = "複製連結").click()
    sleep(1)
    poco(desc = "搜尋").click()
    sleep(1)
    poco(text = "搜尋 YouTube").long_click(duration = 1)
    sleep(1)
    poco.click([0.12, 0.125])
    sleep(1)

    youtube_url = poco(type = "android.widget.EditText").get_text()
    sleep(1)
    keyevent('BACK')
    sleep(1)
    keyevent('BACK')
    
    return youtube_url    
    
    
    
def main():
    
    path = input('請輸入影片放置路徑(ex:E:/Video/) :')
#     push_video_in_mobile(path)
#     find_utube()
    post_video(path)

if __name__ == '__main__':
    main()
