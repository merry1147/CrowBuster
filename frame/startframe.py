import tkinter as tk
from tkinter import font
import threading
from PIL import Image,ImageTk
from execframe import ExecuteFrame
from settingframe import SettingFrame
import configparser
import datetime


import time
import schedule
import os
class StartFrame(tk.Frame):
    def __init__(self,master=None,**kwargs):
        tk.Frame.__init__(self,master,**kwargs,width=700,height=700)
        self.label = tk.Label(self,text="Crow Buster System",font=font.Font(family ="Times",size=35))
        self.start_button = tk.Button(self,text="Start",font=font.Font(size=45),height=2,command=self.Start)
        self.set_button = tk.Button(self,text="Setting",font=font.Font(size=45),height=2,command=self.Setting)
        self.label.place(anchor=tk.CENTER,x=350,y=30)
        self.start_button.place(anchor=tk.CENTER,x=350,y=250,width=270,height=200)
        self.set_button.place(anchor=tk.CENTER,x=350,y=450,width=270,height=200)
        self.set_config()
        
        self.hour2sec=3600
        self.min2sec=60
        config_dict=self.Read_Config()
        self.select_sound=None
        
        self.time=config_dict["time"]
        self.st_time=config_dict["st_time"].split(":")
        self.ed_time=config_dict["ed_time"].split(":")
        self.afterID=None
        self.e_frame = ExecuteFrame(self)
        self.set_frame = SettingFrame(start_f=self)
        self.exec_timer()
        
        #self.time_chenger(self.st_time)
        #threading.Thread(target=self.time_start).start()
    def exec_timer(self):
        if self.time == "1":
            self.afterID=self.after(self.time_chenger(self.st_time),self.Start)
            #print("exec_start")
            #print(self.afterID)


    def create_config(self):
        #print("create config")
        config = configparser.RawConfigParser()
        section1 = "exec"
        config.add_section(section1)
        config.set(section1,"sound")
        config.set(section1,"time","0")
        config.set(section1,"st_time","00:00")
        config.set(section1,"ed_time","00:00")
        with open("./config/config.ini","w") as f:
            config.write(f)
    def set_config(self):
        if not os.path.isdir("./config"):
            os.mkdir("./config")
        if not os.path.exists("./config/config.ini"):
            self.create_config()
        
        config = configparser.SafeConfigParser()
        config.read("./config/config.ini")

        section1 = "exec"
        if not config.has_section(section1):
            self.create_config()
            config.read("./config/config.ini")
        if not  config.has_option(section1,"sound") or not config.has_option(section1,"time") or not config.has_option(section1,"st_time") or not config.has_option(section1,"ed_time"):
            self.create_config()
            config.read("./config/config.ini")
        self.sound_path = config.get(section1,"sound")
        
    def Read_Config(self):
        config = configparser.ConfigParser()
        config.read("./config/config.ini")

        section1 = "exec"
        config_dict = {}
        config_dict["sound"] = config[section1]["sound"]
        config_dict["time"] = config[section1]["time"]
        config_dict["st_time"] = config[section1]["st_time"]
        config_dict["ed_time"] = config[section1]["ed_time"]
        #config_list = [config.get(section1,"camera_view"), config.get(section1,"sound_support")]
        return config_dict

    #ジェスチャ認識を実行
    def Start(self):
        if self.time == "1":
            self.after_cancel(self.afterID)
        self.pack_forget()
        self.e_frame.set_config()
        threading.Thread(target=self.e_frame.Start).start()
        
    
    #設定画面へ移行
    def Setting(self):
        if self.time == "1":
            self.after_cancel(self.afterID)
        config_dict=self.Read_Config()
        self.select_sound=config_dict["sound"].split(",")
        #print("setting")
        #print(self.select_sound)
        self.pack_forget()
        threading.Thread(target=self.set_frame.Start).start()
    
    def time_chenger(self,set_tiem):
        dt_now = datetime.datetime.now()
        d1 = datetime.datetime(year=1970,month=1,day=1,hour=dt_now.hour,minute=dt_now.minute)
        day=1
        if dt_now.hour>int(set_tiem[0]) or (dt_now.hour==int(set_tiem[0]) and dt_now.minute>int(set_tiem[1])):
            day = 2

        d2 = datetime.datetime(year=1970,month=1,day=day,hour=int(set_tiem[0]),minute=int(set_tiem[1]))
        time=(d2-d1)
        #print(time)
        return time.seconds*1000

        
        
    
