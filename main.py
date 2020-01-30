
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import datetime
import time
import re
import Black_Get
import os
import threading
import subprocess

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list_min = []
        self.list_black = []
        self.time_limit = 300
        self.time_new = 7200
        self.file_path = " "
        self.file_path_main = "f:/pynew/text1/addons.py"
        self.file_path_mu = ' '
        self.daili_flag = 0
        self.creatUI()
        self.string = "b'127.0.0.1"
        self.string1 = "b'        "
        self.string2 = "b' <<"
        self.string3 = "b'::ffff:127.0.0.1"

    def creatUI(self):
        self.title("网络过滤器---作者：B17070117")

        frm4 = tk.Frame(self)
        self.label_log = tk.Label(frm4, text='工作日志').pack(side=tk.TOP, fill=tk.X)
        self.text_show = tk.Text(frm4, width=100, height=15)
        self.text_show.pack()
        frm4.grid(row=0, column=0,columnspan=3)

        self.init_time()
        self.init_min()
        self.init_black()

        frm1 = tk.Frame(self)
        self.label_time_int = tk.Label(frm1, text='上网时间设置').pack(side=tk.TOP, fill=tk.X)
        self.entry_time_int_h = ttk.Entry(frm1, show=None, font=('Arial', 14), width=2)
        self.entry_time_int_h.pack(side=tk.LEFT, expand=tk.YES)
        self.entry_time_int_h.insert(tk.END, "0")
        self.label_time_int1 = tk.Label(frm1, text='时', height=4).pack(side=tk.LEFT)
        self.entry_time_int_min = ttk.Entry(frm1, show=None, font=('Arial', 14), width=2)
        self.entry_time_int_min.pack(side=tk.LEFT, expand=tk.YES)
        self.entry_time_int_min.insert(tk.END, "5")
        self.label_time_int2 = tk.Label(frm1, text='分', height=4).pack(side=tk.LEFT)
        self.bt_time_int = ttk.Button(frm1, text="设置时间", command=self.time_set)
        self.bt_time_int.pack(side=tk.LEFT, fill=tk.X)
        frm1.grid(row=1, column=0)

        frm2 = tk.Frame(self)
        self.label_black = tk.Label(frm2, text='黑名单更新时间设置').pack(side=tk.TOP, fill=tk.X)
        self.entry_time_black_h = ttk.Entry(frm2, show=None, font=('Arial', 14), width=2)
        self.entry_time_black_h.pack(side=tk.LEFT, expand=tk.YES)
        self.entry_time_black_h.insert(tk.END, "4")
        self.label_time_black1 = tk.Label(frm2, text='时', height=4).pack(side=tk.LEFT)
        self.entry_time_black_min = ttk.Entry(frm2, show=None, font=('Arial', 14), width=2)
        self.entry_time_black_min.pack(side=tk.LEFT, expand=tk.YES)
        self.entry_time_black_min.insert(tk.END, "0")
        self.label_time_black2 = tk.Label(frm2, text='分', height=4).pack(side=tk.LEFT)
        self.bt_time_black = ttk.Button(frm2, text="设置时间", command=self.time_set_black)
        self.bt_time_black.pack(side=tk.LEFT, fill=tk.X)
        frm2.grid(row=1, column=1)

        frm3 = tk.Frame(self)

        self.label_min = tk.Label(frm3, text='敏感词汇设置').pack(side=tk.TOP, fill=tk.X)
        number = tk.StringVar()
        self.combox_min=ttk.Combobox(frm3,textvariable=number)
        self.combox_min['values']=self.list_min
        self.combox_min.pack(side=tk.LEFT)
        self.bt_min_shan = ttk.Button(frm3, text="删除", command=self.min_shan)
        self.bt_min_shan.pack(side=tk.LEFT, fill=tk.X)
        self.bt_min_tian = ttk.Button(frm3, text="增加", command=self.min_tian)
        self.bt_min_tian.pack(fill=tk.X)
        frm3.grid(row=2, column=1)

        frm5 = tk.Frame(self)
        self.label_black_show = tk.Label(frm5, text='黑名单设置', width=30).pack(side=tk.TOP, fill=tk.X)
        number1 = tk.StringVar()
        self.combox_black = ttk.Combobox(frm5, textvariable=number1)
        self.combox_black['values'] = self.list_black
        self.combox_black.pack(side=tk.LEFT)
        self.bt_black_shan = ttk.Button(frm5, text="删除", command=self.black_shan)
        self.bt_black_shan.pack(side=tk.LEFT, fill=tk.X)
        self.bt_black_tian = ttk.Button(frm5, text="增加", command=self.black_tian)
        self.bt_black_tian.pack(fill=tk.X)
        frm5.grid(row=2, column=0)

        frm6 = tk.Frame(self)
        self.label_liulanqi = tk.Label(frm6, text='浏览器路径设置', width=30).pack(side=tk.TOP, fill=tk.X)
        self.entry_liulanqi = tk.Entry(frm6, show=None, font=('Arial', 10), width=15)
        self.entry_liulanqi.pack(side=tk.LEFT, expand=tk.YES)
        self.bt_liulan = ttk.Button(frm6, text="浏览浏览器", command=self.liulan)
        self.bt_liulan.pack(side=tk.LEFT, fill=tk.X)
        self.bt_liulan = ttk.Button(frm6, text="保存设置", command=self.save)
        self.bt_liulan.pack(side=tk.LEFT, fill=tk.X)
        self.bt_star = ttk.Button(frm6, text="运行浏览器", command=self.star)
        self.bt_star.pack(side=tk.BOTTOM, fill=tk.X)
        frm6.grid(row=3, column=0)

        frm7 = tk.Frame(self)
        self.label_main = tk.Label(frm7, text='主文件路径设置', width=30).pack(side=tk.TOP, fill=tk.X)
        self.entry_main = ttk.Entry(frm7, show=None, font=('Arial', 10), width=15)
        self.entry_main.pack(side=tk.LEFT, expand=tk.YES)
        self.bt_main = ttk.Button(frm7, text="浏览addons.py文件", command=self.main_path)
        self.bt_main.pack(side=tk.LEFT, fill=tk.X)
        self.bt_main = ttk.Button(frm7, text="启动代理", command=self.thread_it(self.daili))
        self.bt_main.pack(side=tk.LEFT, fill=tk.X)
        frm7.grid(row=3, column=1)

    def init_time(self):
        # 输出当前时间
        dt = datetime.datetime.now()
        self.time_str = datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
        self.text_show.insert(tk.END,"Current Time:" + self.time_str + "\n")
        return

    def init_min(self):
        # 加载敏感词汇列表f:/pynew/text1
        file_word = open('./min_word.txt', "r", encoding="utf-8")
        file_word_list = file_word.read().replace("，", "\n").split("\n")
        for line in file_word_list:
            self.list_min.append(line)
        self.text_show.insert(tk.END, "[SUCCESE]Sensitive vocabulary loaded successfully\n")
        return

    def init_black(self):
        # 加载黑名单
        Black_Get.star()
        self.text_show.insert(tk.END, "[SUCCESE]Blacklist updated successfully\n")
        file_black = open('./Black.txt', "r")
        self.list_black = file_black.read().splitlines()
        self.text_show.insert(tk.END, "[SUCCESE]Blacklist loaded successfully\n")
        return


    def time_set(self):
        time_h = int(self.entry_time_int_h.get())
        time_min = int(self.entry_time_int_min.get())
        self.time_limit = time_h * 3600 + time_min * 60
        if (time_min < 0 or time_min > 60):
            str1 = "[ERROR]Internet time setting error\n"
        else:
            str1 = "[SUCCESE]Time set successfully：" + str(self.time_limit) + "s\n"
        self.text_show.insert(tk.END, str1)

    def time_set_black(self):
        time_h = int(self.entry_time_black_h.get())
        time_min = int(self.entry_time_black_min.get())
        self.time_new = time_h * 3600 + time_min * 60
        if (time_min < 0 or time_min > 60):
            str1 = "[ERROR]Blacklist update time setting error\n"
        elif (self.time_new < 7200):
            str1 = "[WARING]The update time is not recommended to be less than 2h\n"
        else:
            str1 = "[SUCCESE]Time set successfully：" + str(self.time_new) + "s\n"
        self.text_show.insert(tk.END, str1)
        return

    def min_shan(self):
        str_com=self.combox_min.get()
        self.list_min.remove(str_com)
        self.combox_min['values']=self.list_min
        self.combox_min.current(0)
        print(self.list_min)
        self.text_show.insert(tk.END, "[SUCCESE]Successfully deleted a sensitive word\n")
        return

    def min_tian(self):
        str_com=self.combox_min.get()
        if (self.list_min.count(str_com) == 0 and str_com != ""):
            self.list_min.insert(0, str_com)
            self.combox_min['values'] = self.list_min
            self.combox_min.current(0)
            self.text_show.insert(tk.END, "[SUCCESE]Successfully added a sensitive word\n")
        else:
            self.text_show.insert(tk.END, "[ERROR]Already exists in the sensitive vocabulary list or is empty\n")
        print(self.list_min)

        return

    def black_shan(self):
        str_com=self.combox_black.get()
        self.list_black.remove(str_com)
        self.combox_black['values']=self.list_black
        self.combox_black.current(0)
        print(self.list_black)
        self.text_show.insert(tk.END, "[SUCCESE]Successfully deleted a blacklist object\n")
        return

    def black_tian(self):
        str_com=self.combox_black.get()
        if (self.list_black.count(str_com) == 0 and str_com != ""):
            self.list_black.insert(0,str_com)
            self.combox_black['values']=self.list_black
            self.combox_black.current(0)
            self.text_show.insert(tk.END, "[SUCCESE]Successfully added a blacklist object\n")
        else:
            self.text_show.insert(tk.END, "[ERROR]Already exists in blacklist or is empty\n")
        print(self.list_black)
        return

    def liulan(self):
        self.file_path = filedialog.askopenfilename()
        self.entry_liulanqi.insert(tk.END, self.file_path)
        self.text_show.insert(tk.END, "[SUCCESE]Get browser path successfully\n")
        return

    def save(self):
        file1 = open("save_data1.txt", 'w', encoding='utf-8')
        file2 = open("save_data2.txt", 'w', encoding='utf-8')
        file3 = open("save_data3.txt", 'w', encoding='utf-8')
        file4 = open("save_data4.txt", 'w', encoding='utf-8')
        for one in self.list_min:
            file1.write(one + '\n')
        for one in self.list_black:
            file2.write(one + "\n")
        file3.write(str(self.time_limit))
        file4.write(str(self.time_new))
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        self.text_show.insert(tk.END, "[SUCCESE]Settings saved successfully\n")
        return

    def main_path(self):
        self.file_path_main = filedialog.askopenfilename()
        self.entry_main.insert(tk.END, self.file_path_main)
        self.text_show.insert(tk.END, "[SUCCESE]Successfully obtained addons.py file path\n")
        self.daili_flag=1
        self.file_path_mu = re.findall("([^\"|^\']+/)addons.py", self.file_path_main)

        # file_data = open("f:/pynew/text1/saving.txt", 'r', encoding="utf-8")
        # str111=file_data.read()
        # self.text_show.insert(tk.END, str111+"\n")
        # file_data.close()

        return

    def daili(self):
        while True:
            #self.text_show.insert(tk.END, "正在检测是否可以启动代理\n")
            if (self.daili_flag!=0):
                self.text_show.insert(tk.END, "Agent started successfully\n")
                cmd = "mitmdump -s %s" % self.file_path_main
                res=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for i in iter(res.stdout.readline, 'b'):
                    if (str(i).startswith(self.string)!=True and str(i).startswith(self.string1)!=True and str(i).startswith(self.string2)!=True and str(i).startswith(self.string3)!=True):
                        print(i)
                        self.text_show.insert(tk.END, str(i)+"\n")
                        self.text_show.see(tk.END)
            time.sleep(3)
        return

    def star(self):
        cmd = '''"%s" --proxy-server=127.0.0.1:8080 --ignore-certificate-errors ''' % self.file_path
        os.popen(cmd)
        self.text_show.insert(tk.END, "Browser started successfully\n")
        return

    @staticmethod
    def thread_it(func):
        t=threading.Thread(target=func)
        t.setDaemon(True)
        t.start()

app = Application()
app.mainloop()
