import mitmproxy.http
from mitmproxy import http
import re
import time
import Black_Get
import WIN_lock


class control:
    def __init__(self):
        file1 = open("f:/pynew/text1/save_data1.txt", 'r', encoding="utf-8")
        file2 = open("f:/pynew/text1/save_data2.txt", 'r', encoding="gbk")
        file3 = open("f:/pynew/text1/save_data3.txt", 'r')
        file4 = open("f:/pynew/text1/save_data4.txt", 'r')
        list_min = file1.read().splitlines()
        list_black = file2.read().splitlines()
        time_limit = int(file3.read())
        time_new = int(file4.read())
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        Black_Get.star()
        self.list_black = list_black
        self.Str_old_list=list_min
        self.time_limit=time_limit
        self.time_new=time_new
        self.list_white = []
        self.time_start = time.time()  # 开始计时
        self.new_count = 0
        self.new_flag = -1
        self.lock_flag=0


    def request(self, flow: mitmproxy.http.HTTPFlow):
        return
    def response(self, flow: mitmproxy.http.HTTPFlow):
        text = flow.response.get_text()
        for Str_pice in self.Str_old_list:
            text = text.replace(Str_pice, "******")
        flow.response.set_text(text)
        time_now=time.time()
        time_c=time_now-self.time_start
        #还有60秒时，每次response提醒
        if (time_c>self.time_limit-60 and time_c<self.time_limit ):
            print("[ATTENTION]"+str(round(self.time_limit-time_c,4))+"seconds left to disconnect!")
        if (time_c>=self.time_limit ):
            print("[ERROR]Time out!")
            flow.response = http.HTTPResponse.make(404)
        #到点计算机锁屏
            if(self.lock_flag==0):
                WIN_lock.lim(self)
                self.lock_flag=1
        # 定期更新黑名单(4h更新一次）
        self.new_count = round(time_c / self.time_new)
        if(self.new_count and self.new_flag!=self.new_count):
            Black_Get.star(self)
            print("NO."+str(self.new_count)+" update blacklist automatically! ")

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if(flow.request.host in self.list_white):
            pass
        else:
            for i in self.list_black:
                if (re.search(i, flow.request.host)):
                    print(flow.request.host)
                    print("[ERROR]This host exists in blacklist, access is forbidden.")
                    flow.response = http.HTTPResponse.make(404)
                    return
        self.list_white.append(flow.request.host)
        print(flow.request.host)
        print("[SUCCESS]This host does not exist in blacklist, access is allowed.")

