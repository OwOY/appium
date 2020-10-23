import codecs

class txt:
    
    def txt_write(title, content):
        
        with codecs.open(f'txt/{title}/content.txt','w','utf-8')as f:
            f.write(content)
            
            
# if __name__ == '__main__':
    
#     title = '沙雕图片（3）'
#     content = '感情测试|你还会单身多久'
#     txt.txt_write(content)