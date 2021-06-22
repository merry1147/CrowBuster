import tkinter as tk
from tkinter import ttk 
from tkinter import font
from tkinter import messagebox
import threading
from PIL import Image,ImageTk
import glob
import os
from playmusic import PlayWavFie
import configparser


select_sound = []
class SettingFrame(tk.Frame):
    def __init__(self,start_f,master=None,**kwargs):
        
        tk.Frame.__init__(self,master,**kwargs,width=700,height=700)
        self.hours_list = [str(date).zfill(2) for date in range(24)]
        self.minutes_list = [str(date).zfill(2) for date in range(60)]

        self.back_button = tk.Button(self,text="back menu",font=font.Font(size=25),command=self.Back)
        self.back_button.place(x=0,y=0)
        self.parent = start_f
        
        self.sound_select = tk.Button(self, text="音設定", font=font.Font(size=25),command=self.sub_window)
        self.sound_select.place(anchor=tk.CENTER,x=350,y=120)
        self.select_sound=None

        self.date = tk.BooleanVar()
        if self.parent.time == "1":
            self.date.set(True)
        self.chkdate = tk.Checkbutton(self,variable=self.date,font=font.Font(size=25),text="指定時刻実行機能を利用する")
        self.chkdate.place(anchor=tk.CENTER,x=350,y=220)


        self.label_st = tk.Label(self, text='開始時刻', font=font.Font(size=25))
        self.label_st.place(anchor=tk.CENTER,x=225,y=270)

        self.st_hours = ttk.Combobox(self, values=self.hours_list, font=font.Font(size=25),width=3)
        self.st_hours.set(self.parent.st_time[0])
        self.st_hours.place(anchor=tk.CENTER,x=310,y=270)

        self.label_colon = tk.Label(self, text=':', font=font.Font(size=25))
        self.label_colon.place(anchor=tk.CENTER,x=350,y=270)

        self.st_minutes = ttk.Combobox(self, values=self.minutes_list, font=font.Font(size=25),width=3)
        self.st_minutes.set(self.parent.st_time[1])
        self.st_minutes.place(anchor=tk.CENTER,x=390,y=270)


        self.label_ed = tk.Label(self, text='終了時刻', font=font.Font(size=25))
        self.label_ed.place(anchor=tk.CENTER,x=225,y=320)

        self.ed_hours = ttk.Combobox(self, values=self.hours_list, font=font.Font(size=25),width=3)
        self.ed_hours.set(self.parent.ed_time[0])
        self.ed_hours.place(anchor=tk.CENTER,x=310,y=320)

        self.label_colon = tk.Label(self, text=':', font=font.Font(size=25))
        self.label_colon.place(anchor=tk.CENTER,x=350,y=320)

        self.ed_minutes = ttk.Combobox(self, values=self.minutes_list, font=font.Font(size=25),width=3)
        self.ed_minutes.set(self.parent.ed_time[1])
        self.ed_minutes.place(anchor=tk.CENTER,x=390,y=320)
        
        
    
    def Start(self):
        self.select_sound=self.parent.select_sound
        
        self.pack()
        
    #ホーム画面へ移行
    def Back(self):
        self.Apply()
        self.pack_forget()
        self.parent.pack()
        self.parent.exec_timer()

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

    def sub_window(self):
        #print(self.parent.sound_path)
        self.sub_win = tk.Toplevel()
        self.sub_win.geometry("300x600")
        select_sound=self.parent.select_sound
        #print(type(select_sound))
        #self.parent.sound_path=self.select_sound
        i=0
        self.path=os.path.abspath('./sound/*.mp3')
        #print(glob.glob(self.path))
        for f in glob.glob(self.path):
            bln = tk.BooleanVar()
            #print(self.select_sound)
            if str(i) in self.select_sound:
                bln.set(True)
            else:
                bln.set(False)
            
            #self.music_path=os.path.split(f)[1]
            chksound = self.ChkSound(pself=self,master=self.sub_win,variable=bln,font=font.Font(size=13),text=os.path.split(f)[1],num=i)
            chksound.place(anchor=tk.W,x=0,y=50+i*25)
            
            playbutton = Button(self.sub_win,text="play",font=font.Font(size=13),path=f)#,command=self.playsound(f))
            playbutton.place(anchor=tk.E,x=250,y=50+i*25)
            #playbutton.bind("<<Button>>",self.playsound(f))
            
            i=i+1
    
    def Apply(self):
        res = messagebox.askyesno("確認","設定を変更しますか？")
        #print(self.parent.sound_path)
        if res:
            
            
            self.select_sound=','.join(self.select_sound)

            self.parent.st_time=[self.st_hours.get(),self.st_minutes.get()]
            self.parent.ed_time=[self.ed_hours.get(),self.ed_minutes.get()]
            
            config = configparser.RawConfigParser()

            section1 = "exec"
            config.add_section(section1)
            config.set(section1,"sound",self.select_sound)
            if self.date.get():
                config.set(section1,"time","1")
                self.parent.time="1"
            else:
                config.set(section1,"time","0")
                self.parent.time="0"
            config.set(section1,"st_time",self.st_hours.get()+":"+self.st_minutes.get())
            config.set(section1,"ed_time",self.ed_hours.get()+":"+self.ed_minutes.get())
            
            #print(self.st_hours.get()+":"+self.st_minutes.get())
            #print(self.ed_hours.get()+":"+self.ed_minutes.get())
            with open("./config/config.ini","w") as f:
                config.write(f)
            self.parent.sound_path = self.select_sound
        
    class ChkSound(tk.Checkbutton):
        def __init__(self,pself,master,variable,font,text,num):
            self.bln=variable
            self.num=num
            self.pself=pself
            super().__init__(
                master=master,
                variable=self.bln,
                font=font,
                text=text,
                command=self.chksound
            )

        def chksound(self):
            
            #print(self.num)
            if str(self.num) in self.pself.select_sound:
                #print(self.pself.select_sound)
                self.pself.select_sound.remove(str(self.num))
                #print("delete:"+str(self.num))
            else:
                #print(self.pself.select_sound)
                self.pself.select_sound.append(str(self.num))
                #print("insert:"+str(self.num))

    
class Button(tk.Button):
    def __init__(self,master,text,font,path):
        self.path=path
        super().__init__(
            master=master,
            text=text,
            font=font,
            command=self.playsound
            )
    
    def playsound(self):
        PlayWavFie(self.path)


        

    

