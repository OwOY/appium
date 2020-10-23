import os


def move_download_and_clean(title):
    
    for xhs_download in os.popen('adb shell "ls /storage/sdcard0/DCIM/Camera/*.mp4"').readlines():
        xhs_download = xhs_download.strip().split('/')[-1]
        
        os.system(f'adb pull /storage/sdcard0/DCIM/Camera/{xhs_download} C:/Users/JM832/Desktop/1/txt/{title}/{xhs_download}')
       
    
    try:
        os.popen('adb shell "rm -r /storage/sdcard0/DCIM/Camera/*.mp4"')
    except:
        pass

def pic_download_and_clean(title):
    
    for xhs_download in os.popen('adb shell "ls /storage/sdcard0/DCIM/Camera/小红书"').readlines():
        xhs_download = xhs_download.strip()
        
            
        os.system(f'adb pull /storage/sdcard0/DCIM/Camera/小红书/{xhs_download} C:/Users/JM832/Desktop/1/txt/{title}/{xhs_download}.jpg')
        

    try:
        os.popen('adb shell "rm -r /storage/sdcard0/DCIM/Camera/*.jpg"')
    except:
        pass
