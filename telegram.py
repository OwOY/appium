# -*- encoding=utf8 -*-
__author__ = "jingm"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import codecs
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)


path = os.getcwd()

class txt:

    def txt_write(content):
        with codecs.open('bet365.txt','a','utf-8')as f:
            f.write(f'{content}\n')
    
    
    
    def txt_read():
        with codecs.open('E:/telegram.air/bet365.txt','r','utf-8')as f:
            content_in_txt = f.readlines()
            _content_in_txt = []
            for content in content_in_txt:
                content = content.strip()
                _content_in_txt.append(content)
            return _content_in_txt
            
            
            
    def check_file():
        if not os.path.isfile('bet365.txt'):
            with codecs.open('bet365.txt','w','utf-8')as f:
                f.write('')


                
# def main():

txt.check_file()
print(f'========================{path}============================')
i = 10
while i<=10:
    try:
        content = poco(name = "androidx.recyclerview.widget.RecyclerView").child(type = "android.view.ViewGroup")[i].get_name()
        content = content.split('\n')[1]
        content_in_txt = txt.txt_read()
        
        if 'Sticker' not in content and 'Photo' not in content and 'Video' not in content and 'GIF' not in content:
            if content not in content_in_txt:
                txt.txt_write(content)

                print(content)
        
    except:
        pass


    i -= 1

    if i < 1:
        i = 10
        poco.swipe([0.5, 0.2], [0.5, 0.7], duration = 0.5)
    sleep(3)
        
