# appium
https://news.tianyancha.com/ll_7oefn63kop.html  

https://www.itread01.com/content/1547310497.html

## mitmdump  
flow.request.headers #获取所有头信息，包含Host、User-Agent、Content-type等字段  
flow.request.url #完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数  
flow.request.pretty_url #同flow.request.url目前没看出什么差别  
flow.request.host #域名  
flow.request.method #请求方式。POST、GET等  
flow.request.scheme #什么请求 ，如https  
flow.request.path # 请求的路径，url除域名之外的内容  
flow.request.get_text() #请求中body内容，有一些http会把请求参数放在body里面，那么可通过此方法获取，返回字典类型  
flow.request.query #返回MultiDictView类型的数据，url直接带的键值参数  
flow.request.get_content()#bytes,结果如flow.request.get_text()  
flow.request.raw_content #bytes,结果如flow.request.get_content()  
flow.request.urlencoded_form #MultiDictView，content-type：application/x-www-form-urlencoded时的请求参数，不包含url直接带的键值参数  
flow.request.multipart_form #MultiDictView，content-type：multipart/form-data  
时的请求参数，不包含url直接带的键值参数  

flow.response.status_code #状态码  
flow.response.text#返回内容，已解码  
flow.response.content #返回内容，二进制  
flow.response.setText()#修改返回内容，不需要转码  

## !!!airtest  
auto_setup(__file__, devices = ['Android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP^&^&ori_method=ADBORI'])  多設備連接  

x.attr(‘desc’)取得特殊屬性值  
x.click()  點擊  
x.get_text()  獲得文本  
swipe([0, 0], [1, 1]) 滑動螢幕(按比例 左上至右下)  
x.exist()  確認元素是否存在  
poco.wait_for_any([a,b,c]) 等待元素存在才繼續  
poco.wait_for_all([a,b,c]) 等待所有元素存在才繼續  

https://www.jianshu.com/p/203eb5f08761 adb 操作  
https://airtest.doc.io.netease.com/   airtest Documents  
https://github.com/AirtestProject/Poco  POCO源碼  
https://www.mdeditor.tw/pl/2iK6/zh-tw  基本介紹  
https://www.cnblogs.com/wutaotaosin/articles/11396827.html  基本操作  
https://www.codenong.com/cs105283799/  進階指令  



## adb 設置  
### 連接nox  
adb -s 127.0.0.1:{port}  

### 喚醒媒體庫  

adb shell "am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard  
adb shell "am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/Video/{video}"  
  
### 強制停止youtube  
am force-stop com.google.android.youtube
