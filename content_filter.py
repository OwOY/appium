import emoji
import string
import re

class filters:

    def content_filter(content):
        
        content = emoji.demojize(content, delimiters=(':',':'))
        content = content.replace('不喜欢','')
        return content


    def title_filter(title):
        
        
        
        title = emoji.demojize(title, delimiters=(':',':'))
        title = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", title)
        
        return title
    
    
# if __name__ == '__main__':
    
#     title = '这样撩女生，女生会心动爱上你'
#     title = filters.title_filter(title)
#     print(title)