import time
import keyboard
from PIL import ImageGrab
import pytesseract
from PIL import Image

# 3.调用百度的接口识别图片内容
from aip import AipOcr

"""你的APPID AK SK"""
APP_ID = "25130636"
API_KEY = "d82FLLKD1REDjEIR7GqmG9ve"
SECRET_KEY = "Gdo6lGbagDgr01RbuGekwwf7FYc0zwPU"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
class baidu_ocr(object):
    def __init__(self):
        """你的APPID AK SK"""
        APP_ID = "25130636"
        API_KEY = "d82FLLKD1REDjEIR7GqmG9ve"
        SECRET_KEY = "Gdo6lGbagDgr01RbuGekwwf7FYc0zwPU"
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        self.key_list=[]
        self.key_str=""
        self.value_list=[]
        self.value_str=""
        self.enter_count=0

    def baidu_ocr(self):
        while True:
            # 截图
            keyboard.wait(hotkey="alt+ctrl+a")  # 等待键盘的触发。等待QQ截图
            keyboard.wait(hotkey="enter")
            time.sleep(0.1)

            # 图片保存
            image = ImageGrab.grabclipboard()  # 获取剪切板的图片
            image.save('screen.jpg')  # 图片保存

            # 打开screen.jpg图片，以read bytes方式进行操作
            with open('screen.jpg', 'rb') as f:
                image = f.read()  # image就是这张图片的二进制内容
                text = self.client.basicAccurate(image)  # 调用百度的接口帮我们识别图片的内容
                #print(text)
                result = text['words_result']  # 获取返回内容的字典
                # 遍历输出字典内容
                for i in result:
                    self.key_list.append(i["words"])
                    if self.key_str=="":
                        self.key_str=self.key_str+i["words"]
                    else:
                        self.key_str = self.key_str +","+ i["words"]

                with open("./value.dat", "w") as f:
                    f.writelines(self.key_str)
                self.enter_count += 1
                self.key_str = ""

                if True:
                    self.enter_count=0
                    keyboard.wait(hotkey="alt+ctrl+e")  # 等待键盘的触发。等待QQ截图
                    time.sleep(0.1)
                    self.orc_join()

    def Get_key(self):
        while True:
            # 截图
            keyboard.wait(hotkey="alt+ctrl+a")  # 等待键盘的触发。等待QQ截图
            keyboard.wait(hotkey="enter")
            time.sleep(0.1)

            # 图片保存
            image = ImageGrab.grabclipboard()  # 获取剪切板的图片
            image.save('screen.jpg')  # 图片保存

            # 打开screen.jpg图片，以read bytes方式进行操作
            with open('screen.jpg', 'rb') as f:
                image = f.read()  # image就是这张图片的二进制内容
                text = self.client.basicAccurate(image)  # 调用百度的接口帮我们识别图片的内容
                #print(text)
                result = text['words_result']  # 获取返回内容的字典
                # 遍历输出字典内容
                for i in result:
                    self.key_list.append(i["words"])
                    if self.key_str=="":
                        self.key_str=self.key_str+i["words"]
                    else:
                        self.key_str = self.key_str +","+ i["words"]
                if self.enter_count==0:
                    with open("./key.dat","w") as f:
                        f.writelines(self.key_str)
                        f.close()
                    self.enter_count+=1
                    self.key_str=""
                    break

    def orc_join(self):
        dict={}
        with open("./value.dat", "r") as f:
            value=f.readlines()
            print(value)
        with open("./key.dat", "r") as f:
            key=f.readlines()
            print(key)
        key_list=key[0].split(",")
        value_list=value[0].split(",")
        for i ,j in zip(key_list,value_list):
            if len(key)==len(value):
                dict[i]=j
        print(dict)







def pytesseract_ocr():
    while True:
        # 截图
        keyboard.wait(hotkey="alt+ctrl+a")  # 等待键盘的触发。等待QQ截图
        keyboard.wait(hotkey="enter")
        time.sleep(0.1)

        # 图片保存
        image = ImageGrab.grabclipboard()  # 获取剪切板的图片
        image.save('screen.jpg')  # 图片保存


        img = Image.open('screen.jpg')
        pytesseract.pytesseract.tesseract_cmd = 'd:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
        s = pytesseract.image_to_string(img, lang='chi_sim')  # 不加lang参数的话，默认进行英文识别
        print(s)


#pytesseract_ocr()
new=baidu_ocr()
new.Get_key()
new.baidu_ocr()