# -*- encoding=utf8 -*-
__author__ = "jingm"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os
import codecs
import pymongo
from datetime import datetime


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

path = os.getcwd()

class mongodb:
    
    client = pymongo.MongoClient("mongodb+srv://jingmai832:1234@telegram.2tgdz.mongodb.net/telegram?retryWrites=true&w=majority")
    db = client.airtest
    collection = db.telegram_talkNBA
    
    
        
    def get_mongo_ID(self):
        
        data = self.collection.find({})
        total = []
        for d in data:
            total.append(d)
        return len(total)
    
    
    def insert_mongo(self, ID, telegram_ID, content, timestamp):



        DB_dict = {'ID' : ID,
                   'telegram_ID' : telegram_ID,
                   'text' : content,
                   'timestamp' : timestamp}

        self.collection.insert_one(DB_dict)

        return 'Insert OK'


class txt:

    def txt_write(content):
        with codecs.open('talkNBA.txt','a','utf-8')as f:
            f.write(f'{content}\n')
    
    
    
    def txt_read():
        with codecs.open('talkNBA.txt','r','utf-8')as f:
            content_in_txt = f.readlines()
            _content_in_txt = []
            for content in content_in_txt:
                content = content.strip()
                _content_in_txt.append(content)
            return _content_in_txt
            
            
            
    def check_file():
        if not os.path.isfile('talkNBA.txt'):
            with codecs.open('talkNBA.txt','w','utf-8')as f:
                f.write('')


                
# def main():

txt.check_file()
print(f'========================{path}============================')
i = 10
ID = mongodb().get_mongo_ID + 1
while i<=10:
    try:
        content = poco(name = "androidx.recyclerview.widget.RecyclerView").child(type = "android.view.ViewGroup")[i].get_name()
        
        telegram_ID = content.split('\n')[0]
        content = content.split('\n')[1]
        timestamp = datetime.now().timestamp()
        
        content_in_txt = txt.txt_read()

        if 'Sticker' not in content and 'Photo' not in content and 'Video' not in content and 'GIF' not in content:
            if content not in content_in_txt:
                txt.txt_write(content)
                
                
                print(content)
                
                mongodb().insert_mongo(ID, telegram_ID, content, timestamp)
                ID += 1
    except:
        pass


    i -= 1

    if i < 1:
        i = 10
        poco.swipe([0.5, 0.2], [0.5, 0.7], duration = 0.5)
#     sleep(1)s
        
