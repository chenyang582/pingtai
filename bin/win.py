#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Nov 03, 2020 03:07:33 PM CST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.messagebox



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()



class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1196x621+191+55")
        top.minsize(180, 1)
        top.maxsize(1924, 1050)
        top.resizable(0, 0)
        top.title("众包平台型公司税负及盈利模型测算")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        #校验函数，校验输入是否为数字的函数。测试时发现类中不能加self,暂不确定是不是属于静态方法
        def test():
            try:
                float(self.Entry1.get())
                pass
            except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
                return False
            try:  # 个体户数必须是整数
                int(self.Entry1_3.get())
                pass
            except ValueError:
                return False
            try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
                float(self.Entry1_4.get())
                pass
            except ValueError:
                return False


            if float(self.Entry1.get()) < 0:
                return False
            elif int(self.Entry1_3.get()) < 0:
                return False
            elif float(self.Entry1_4.get()) < 0:
                return False
            elif float(self.Entry1.get()) > 10000000:
                return False
            elif int(self.Entry1_3.get()) > 10000:
                return False
            elif float(self.Entry1_4.get()) > 10000000:
                return False
            return True


            #处理函数，将输入框完全清空
        def deleteentry():
            self.Entry1.delete(0, "end")
            self.Entry1.insert(0,'0')

            self.Entry1_3.delete(0, "end")
            self.Entry1_3.insert(0,'1')

            self.Entry1_4.delete(0, "end")
            self.Entry1_4.insert(0,'0')

            tk.messagebox.showerror('输入错误提示', '不能输入文字或者负数呀，并且个体户必须是整数，不然怎么计算…')


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.025, rely=0.016, height=43, width=375)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {苹方 常规} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#f17712")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''众包平台型公司税负及盈利模型测算V1.2''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.435, rely=0.411, relheight=0.006
                , relwidth=0.561)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#000000")
        self.Frame1.configure(highlightcolor="#000000")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.426, rely=0.048, height=27, width=180)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {苹方 常规} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2.configure(foreground="#f17712")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''平台公司与外部的总包项目''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.426, rely=0.097, height=38, width=167)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {苹方 常规} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''开具发票金额（元）''')

        #开具发票金额
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.564, rely=0.098,height=34, relwidth=0.137)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        self.Entry1.insert(0,'0')
        self.Entry1.configure(validate="focusout")
        self.Entry1.configure(validatecommand=test)
        self.Entry1.configure(invalidcommand=deleteentry)

        self.Labelframe1_2 = tk.LabelFrame(top)
        self.Labelframe1_2.place(relx=0.426, rely=0.177, relheight=0.198
                , relwidth=0.174)
        self.Labelframe1_2.configure(relief='groove')
        self.Labelframe1_2.configure(foreground="black")
        self.Labelframe1_2.configure(text='''所得税税点''')
        self.Labelframe1_2.configure(background="#d9d9d9")
        self.Labelframe1_2.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_2.configure(highlightcolor="black")

        self.v1 = tk.DoubleVar()
        self.v1.set(0.25)

        self.Radiobutton1_3 = tk.Radiobutton(self.Labelframe1_2)
        self.Radiobutton1_3.place(relx=-0.096, rely=0.276, relheight=0.293
                , relwidth=0.74, bordermode='ignore')
        self.Radiobutton1_3.configure(activebackground="#ececec")
        self.Radiobutton1_3.configure(activeforeground="#000000")
        self.Radiobutton1_3.configure(background="#d9d9d9")
        self.Radiobutton1_3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_3.configure(foreground="#000000")
        self.Radiobutton1_3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_3.configure(highlightcolor="black")
        self.Radiobutton1_3.configure(justify='left')
        self.Radiobutton1_3.configure(text='''25%''')
        self.Radiobutton1_3.configure(variable=self.v1)
        self.Radiobutton1_3.configure(value=0.25)

        self.Radiobutton2_4 = tk.Radiobutton(self.Labelframe1_2)
        self.Radiobutton2_4.place(relx=0.433, rely=0.301, relheight=0.244
                , relwidth=0.51, bordermode='ignore')
        self.Radiobutton2_4.configure(activebackground="#ececec")
        self.Radiobutton2_4.configure(activeforeground="#000000")
        self.Radiobutton2_4.configure(background="#d9d9d9")
        self.Radiobutton2_4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_4.configure(foreground="#000000")
        self.Radiobutton2_4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_4.configure(highlightcolor="black")
        self.Radiobutton2_4.configure(justify='left')
        self.Radiobutton2_4.configure(text='''20%''')
        self.Radiobutton2_4.configure(variable=self.v1)
        self.Radiobutton2_4.configure(value=0.20)

        self.Radiobutton3 = tk.Radiobutton(self.Labelframe1_2)
        self.Radiobutton3.place(relx=0.077, rely=0.545, relheight=0.293
                , relwidth=0.389, bordermode='ignore')
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(text='''15%''')
        self.Radiobutton3.configure(variable=self.v1)
        self.Radiobutton3.configure(value=0.15)

        self.Labelframe1_5 = tk.LabelFrame(top)
        self.Labelframe1_5.place(relx=0.61, rely=0.177, relheight=0.198
                , relwidth=0.181)
        self.Labelframe1_5.configure(relief='groove')
        self.Labelframe1_5.configure(foreground="black")
        self.Labelframe1_5.configure(text='''专用发票税点''')
        self.Labelframe1_5.configure(background="#d9d9d9")
        self.Labelframe1_5.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_5.configure(highlightcolor="black")

        self.v2 = tk.DoubleVar()
        self.v2.set(0.06)

        self.Radiobutton1_6 = tk.Radiobutton(self.Labelframe1_5)
        self.Radiobutton1_6.place(relx=0.138, rely=0.325, relheight=0.171
                , relwidth=0.382, bordermode='ignore')
        self.Radiobutton1_6.configure(activebackground="#ececec")
        self.Radiobutton1_6.configure(activeforeground="#000000")
        self.Radiobutton1_6.configure(background="#d9d9d9")
        self.Radiobutton1_6.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_6.configure(foreground="#000000")
        self.Radiobutton1_6.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_6.configure(highlightcolor="black")
        self.Radiobutton1_6.configure(justify='left')
        self.Radiobutton1_6.configure(text='''13%''')
        self.Radiobutton1_6.configure(variable=self.v2)
        self.Radiobutton1_6.configure(value=0.13)

        self.Radiobutton2_17 = tk.Radiobutton(self.Labelframe1_5)
        self.Radiobutton2_17.place(relx=0.484, rely=0.325, relheight=0.171
                , relwidth=0.392, bordermode='ignore')
        self.Radiobutton2_17.configure(activebackground="#ececec")
        self.Radiobutton2_17.configure(activeforeground="#000000")
        self.Radiobutton2_17.configure(background="#d9d9d9")
        self.Radiobutton2_17.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_17.configure(foreground="#000000")
        self.Radiobutton2_17.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_17.configure(highlightcolor="black")
        self.Radiobutton2_17.configure(justify='left')
        self.Radiobutton2_17.configure(text='''9%''')
        self.Radiobutton2_17.configure(variable=self.v2)
        self.Radiobutton2_17.configure(value=0.09)

        self.Radiobutton2_8 = tk.Radiobutton(self.Labelframe1_5)
        self.Radiobutton2_8.place(relx=0.065, rely=0.577, relheight=0.163
                , relwidth=0.488, bordermode='ignore')
        self.Radiobutton2_8.configure(activebackground="#ececec")
        self.Radiobutton2_8.configure(activeforeground="#000000")
        self.Radiobutton2_8.configure(background="#d9d9d9")
        self.Radiobutton2_8.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_8.configure(foreground="#000000")
        self.Radiobutton2_8.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_8.configure(highlightcolor="black")
        self.Radiobutton2_8.configure(justify='left')
        self.Radiobutton2_8.configure(text='''6%''')
        self.Radiobutton2_8.configure(variable=self.v2)
        self.Radiobutton2_8.configure(value=0.06)

        self.Radiobutton2_1 = tk.Radiobutton(self.Labelframe1_5)
        self.Radiobutton2_1.place(relx=0.479, rely=0.569, relheight=0.163
                , relwidth=0.396, bordermode='ignore')
        self.Radiobutton2_1.configure(activebackground="#ececec")
        self.Radiobutton2_1.configure(activeforeground="#000000")
        self.Radiobutton2_1.configure(background="#d9d9d9")
        self.Radiobutton2_1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_1.configure(foreground="#000000")
        self.Radiobutton2_1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_1.configure(highlightcolor="black")
        self.Radiobutton2_1.configure(justify='left')
        self.Radiobutton2_1.configure(text='''3%''')
        self.Radiobutton2_1.configure(variable=self.v2)
        self.Radiobutton2_1.configure(value=0.03)

        self.Label2_10 = tk.Label(top)
        self.Label2_10.place(relx=0.426, rely=0.432, height=36, width=180)
        self.Label2_10.configure(activebackground="#f9f9f9")
        self.Label2_10.configure(activeforeground="black")
        self.Label2_10.configure(background="#d9d9d9")
        self.Label2_10.configure(disabledforeground="#a3a3a3")
        self.Label2_10.configure(font="-family {苹方 常规} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_10.configure(foreground="#f17712")
        self.Label2_10.configure(highlightbackground="#d9d9d9")
        self.Label2_10.configure(highlightcolor="black")
        self.Label2_10.configure(text='''平台公司与个体户的分包项目''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.450, rely=0.491, height=29, width=206)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {苹方 常规} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''核定征收个体户（户）''')

        #个体户数
        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(relx=0.61, rely=0.49,height=34, relwidth=0.162)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="blue")
        self.Entry1_3.configure(selectforeground="white")
        self.Entry1_3.insert(0,'0')
        self.Entry1_3.configure(validate="focusout")
        self.Entry1_3.configure(validatecommand=test)
        self.Entry1_3.configure(invalidcommand=deleteentry)

        self.Label2_3 = tk.Label(top)
        self.Label2_3.place(relx=0.435, rely=0.549, height=38, width=206)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font="-family {苹方 常规} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''每户每年开具发票金额（元）''')

        #每户开具的金额数
        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(relx=0.61, rely=0.559,height=34, relwidth=0.162)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="blue")
        self.Entry1_4.configure(selectforeground="white")
        self.Entry1_4.insert(0,'0')
        self.Entry1_4.configure(validate="focusout")
        self.Entry1_4.configure(validatecommand=test)
        self.Entry1_4.configure(invalidcommand=deleteentry)

        self.Labelframe1_3 = tk.LabelFrame(top)
        self.Labelframe1_3.place(relx=0.426, rely=0.628, relheight=0.198
                , relwidth=0.174)
        self.Labelframe1_3.configure(relief='groove')
        self.Labelframe1_3.configure(foreground="black")
        self.Labelframe1_3.configure(text='''发票类型''')
        self.Labelframe1_3.configure(background="#d9d9d9")
        self.Labelframe1_3.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_3.configure(highlightcolor="black")

        self.v3 = tk.DoubleVar()
        self.v3.set(0)

        self.Radiobutton1_4 = tk.Radiobutton(self.Labelframe1_3)
        self.Radiobutton1_4.place(relx=0.05, rely=0.285, relheight=0.301
                , relwidth=0.739, bordermode='ignore')
        self.Radiobutton1_4.configure(activebackground="#ececec")
        self.Radiobutton1_4.configure(activeforeground="#000000")
        self.Radiobutton1_4.configure(background="#d9d9d9")
        self.Radiobutton1_4.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_4.configure(foreground="#000000")
        self.Radiobutton1_4.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_4.configure(highlightcolor="black")
        self.Radiobutton1_4.configure(justify='left')
        self.Radiobutton1_4.configure(text='''普通发票''')
        self.Radiobutton1_4.configure(variable=self.v3)
        self.Radiobutton1_4.configure(value=0)

        self.Radiobutton2_5 = tk.Radiobutton(self.Labelframe1_3)
        self.Radiobutton2_5.place(relx=-0.005, rely=0.585, relheight=0.252
                , relwidth=0.844, bordermode='ignore')
        self.Radiobutton2_5.configure(activebackground="#ececec")
        self.Radiobutton2_5.configure(activeforeground="#000000")
        self.Radiobutton2_5.configure(background="#d9d9d9")
        self.Radiobutton2_5.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_5.configure(foreground="#000000")
        self.Radiobutton2_5.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_5.configure(highlightcolor="black")
        self.Radiobutton2_5.configure(justify='left')
        self.Radiobutton2_5.configure(text='''专用发票''')
        self.Radiobutton2_5.configure(variable=self.v3)
        self.Radiobutton2_5.configure(value=1)

        self.Label2_11 = tk.Label(top)
        self.Label2_11.place(relx=0.025, rely=0.071, height=35, width=92)
        self.Label2_11.configure(activebackground="#f9f9f9")
        self.Label2_11.configure(activeforeground="black")
        self.Label2_11.configure(background="#d9d9d9")
        self.Label2_11.configure(disabledforeground="#a3a3a3")
        self.Label2_11.configure(font="-family {苹方 常规} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_11.configure(foreground="#404040")
        self.Label2_11.configure(highlightbackground="#d9d9d9")
        self.Label2_11.configure(highlightcolor="black")
        self.Label2_11.configure(text='''模型展示''')


        #滚动条
        self.Scrollbar1 = tk.Scrollbar(top)
        self.Scrollbar1.pack(side="right", fill="y")

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.033, rely=0.129, relheight=0.789, relwidth=0.371)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")
        self.Text1.configure(yscrollcommand=self.Scrollbar1.set)
        self.Text1.tag_config("tag_1", font="-family {微软雅黑} -size 10 -weight bold")
        self.Text1.tag_config("tag_2", font="-family {微软雅黑} -size 9 -weight bold")

        self.Scrollbar1.configure(command=self.Text1.yview)


        self.Labelframe1_6 = tk.LabelFrame(top)
        self.Labelframe1_6.place(relx=0.61, rely=0.628, relheight=0.198
                , relwidth=0.181)
        self.Labelframe1_6.configure(relief='groove')
        self.Labelframe1_6.configure(foreground="black")
        self.Labelframe1_6.configure(text='''核定征收率''')
        self.Labelframe1_6.configure(background="#d9d9d9")
        self.Labelframe1_6.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_6.configure(highlightcolor="black")

        self.v4 = tk.DoubleVar()
        self.v4.set(0.10)

        self.Radiobutton1_7 = tk.Radiobutton(self.Labelframe1_6)
        self.Radiobutton1_7.place(relx=0.138, rely=0.309, relheight=0.171
                , relwidth=0.382, bordermode='ignore')
        self.Radiobutton1_7.configure(activebackground="#ececec")
        self.Radiobutton1_7.configure(activeforeground="#000000")
        self.Radiobutton1_7.configure(background="#d9d9d9")
        self.Radiobutton1_7.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_7.configure(foreground="#000000")
        self.Radiobutton1_7.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_7.configure(highlightcolor="black")
        self.Radiobutton1_7.configure(justify='left')
        self.Radiobutton1_7.configure(text='''13%''')
        self.Radiobutton1_7.configure(variable=self.v4)
        self.Radiobutton1_7.configure(value=0.13)

        self.Radiobutton2_2 = tk.Radiobutton(self.Labelframe1_6)
        self.Radiobutton2_2.place(relx=0.484, rely=0.309, relheight=0.171
                , relwidth=0.392, bordermode='ignore')
        self.Radiobutton2_2.configure(activebackground="#ececec")
        self.Radiobutton2_2.configure(activeforeground="#000000")
        self.Radiobutton2_2.configure(background="#d9d9d9")
        self.Radiobutton2_2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_2.configure(foreground="#000000")
        self.Radiobutton2_2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_2.configure(highlightcolor="black")
        self.Radiobutton2_2.configure(justify='left')
        self.Radiobutton2_2.configure(text='''12%''')
        self.Radiobutton2_2.configure(variable=self.v4)
        self.Radiobutton2_2.configure(value=0.12)

        self.Radiobutton2_9 = tk.Radiobutton(self.Labelframe1_6)
        self.Radiobutton2_9.place(relx=0.088, rely=0.569, relheight=0.163
                , relwidth=0.488, bordermode='ignore')
        self.Radiobutton2_9.configure(activebackground="#ececec")
        self.Radiobutton2_9.configure(activeforeground="#000000")
        self.Radiobutton2_9.configure(background="#d9d9d9")
        self.Radiobutton2_9.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_9.configure(foreground="#000000")
        self.Radiobutton2_9.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_9.configure(highlightcolor="black")
        self.Radiobutton2_9.configure(justify='left')
        self.Radiobutton2_9.configure(text='''11%''')
        self.Radiobutton2_9.configure(variable=self.v4)
        self.Radiobutton2_9.configure(value=0.11)

        self.Radiobutton2_3 = tk.Radiobutton(self.Labelframe1_6)
        self.Radiobutton2_3.place(relx=0.479, rely=0.569, relheight=0.163
                , relwidth=0.396, bordermode='ignore')
        self.Radiobutton2_3.configure(activebackground="#ececec")
        self.Radiobutton2_3.configure(activeforeground="#000000")
        self.Radiobutton2_3.configure(background="#d9d9d9")
        self.Radiobutton2_3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_3.configure(foreground="#000000")
        self.Radiobutton2_3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_3.configure(highlightcolor="black")
        self.Radiobutton2_3.configure(justify='left')
        self.Radiobutton2_3.configure(text='''10%''')
        self.Radiobutton2_3.configure(variable=self.v4)
        self.Radiobutton2_3.configure(value=0.10)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.426, rely=0.86, height=40, width=205)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''立即测算''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.617, rely=0.86, height=40, width=205)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''清空数据''')


        self.v5 = tk.DoubleVar()
        self.v5.set(0.001)
        #总包合同印花税
        self.Labelframe1_1 = tk.LabelFrame(top)
        self.Labelframe1_1.place(relx=0.803, rely=0.177, relheight=0.198
                , relwidth=0.181)
        self.Labelframe1_1.configure(relief='groove')
        self.Labelframe1_1.configure(foreground="black")
        self.Labelframe1_1.configure(text='印花税税点（总包合同）')
        self.Labelframe1_1.configure(background="#d9d9d9")
        self.Labelframe1_1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_1.configure(highlightcolor="black")

        self.Radiobutton1_2 = tk.Radiobutton(self.Labelframe1_1)
        self.Radiobutton1_2.place(relx=0.097, rely=0.325, relheight=0.171
                , relwidth=0.384, bordermode='ignore')
        self.Radiobutton1_2.configure(activebackground="#ececec")
        self.Radiobutton1_2.configure(activeforeground="#000000")
        self.Radiobutton1_2.configure(background="#d9d9d9")
        self.Radiobutton1_2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_2.configure(foreground="#000000")
        self.Radiobutton1_2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_2.configure(highlightcolor="black")
        self.Radiobutton1_2.configure(justify='left')
        self.Radiobutton1_2.configure(text='1‰')
        self.Radiobutton1_2.configure(variable=self.v5)
        self.Radiobutton1_2.configure(value=0.001)


        self.Radiobutton2_30 = tk.Radiobutton(self.Labelframe1_1)
        self.Radiobutton2_30.place(relx=0.463, rely=0.325, relheight=0.171
                , relwidth=0.486, bordermode='ignore')
        self.Radiobutton2_30.configure(activebackground="#ececec")
        self.Radiobutton2_30.configure(activeforeground="#000000")
        self.Radiobutton2_30.configure(background="#d9d9d9")
        self.Radiobutton2_30.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_30.configure(foreground="#000000")
        self.Radiobutton2_30.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_30.configure(highlightcolor="black")
        self.Radiobutton2_30.configure(justify='left')
        self.Radiobutton2_30.configure(text='0.5‰')
        self.Radiobutton2_30.configure(variable=self.v5)
        self.Radiobutton2_30.configure(value=0.0005)


        self.Radiobutton2_41 = tk.Radiobutton(self.Labelframe1_1)
        self.Radiobutton2_41.place(relx=0.079, rely=0.577, relheight=0.163
                , relwidth=0.491, bordermode='ignore')
        self.Radiobutton2_41.configure(activebackground="#ececec")
        self.Radiobutton2_41.configure(activeforeground="#000000")
        self.Radiobutton2_41.configure(background="#d9d9d9")
        self.Radiobutton2_41.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_41.configure(foreground="#000000")
        self.Radiobutton2_41.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_41.configure(highlightcolor="black")
        self.Radiobutton2_41.configure(justify='left')
        self.Radiobutton2_41.configure(text='0.3‰')
        self.Radiobutton2_41.configure(variable=self.v5)
        self.Radiobutton2_41.configure(value=0.0003)

        self.Radiobutton2_07 = tk.Radiobutton(self.Labelframe1_1)
        self.Radiobutton2_07.place(relx=0.546, rely=0.569, relheight=0.171
                , relwidth=0.347, bordermode='ignore')
        self.Radiobutton2_07.configure(activebackground="#ececec")
        self.Radiobutton2_07.configure(activeforeground="#000000")
        self.Radiobutton2_07.configure(background="#d9d9d9")
        self.Radiobutton2_07.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_07.configure(foreground="#000000")
        self.Radiobutton2_07.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_07.configure(highlightcolor="black")
        self.Radiobutton2_07.configure(justify='left')
        self.Radiobutton2_07.configure(text='''不缴纳''')
        self.Radiobutton2_07.configure(variable=self.v5)
        self.Radiobutton2_07.configure(value=0)



        self.v6 = tk.DoubleVar()
        self.v6.set(0.001)
        #分包合同印花税
        self.Labelframe1_20 = tk.LabelFrame(top)
        self.Labelframe1_20.place(relx=0.803, rely=0.628, relheight=0.198
                , relwidth=0.181)
        self.Labelframe1_20.configure(relief='groove')
        self.Labelframe1_20.configure(foreground="black")
        self.Labelframe1_20.configure(text='印花税税点（分包合同）')
        self.Labelframe1_20.configure(background="#d9d9d9")
        self.Labelframe1_20.configure(highlightbackground="#d9d9d9")
        self.Labelframe1_20.configure(highlightcolor="black")

        self.Radiobutton1_31 = tk.Radiobutton(self.Labelframe1_20)
        self.Radiobutton1_31.place(relx=0.093, rely=0.325, relheight=0.171
                , relwidth=0.384, bordermode='ignore')
        self.Radiobutton1_31.configure(activebackground="#ececec")
        self.Radiobutton1_31.configure(activeforeground="#000000")
        self.Radiobutton1_31.configure(background="#d9d9d9")
        self.Radiobutton1_31.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1_31.configure(foreground="#000000")
        self.Radiobutton1_31.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1_31.configure(highlightcolor="black")
        self.Radiobutton1_31.configure(justify='left')
        self.Radiobutton1_31.configure(text='1‰')
        self.Radiobutton1_31.configure(variable=self.v6)
        self.Radiobutton1_31.configure(value=0.001)


        self.Radiobutton2_04 = tk.Radiobutton(self.Labelframe1_20)
        self.Radiobutton2_04.place(relx=0.463, rely=0.325, relheight=0.171
                , relwidth=0.486, bordermode='ignore')
        self.Radiobutton2_04.configure(activebackground="#ececec")
        self.Radiobutton2_04.configure(activeforeground="#000000")
        self.Radiobutton2_04.configure(background="#d9d9d9")
        self.Radiobutton2_04.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_04.configure(foreground="#000000")
        self.Radiobutton2_04.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_04.configure(highlightcolor="black")
        self.Radiobutton2_04.configure(justify='left')
        self.Radiobutton2_04.configure(text='0.5‰')
        self.Radiobutton2_04.configure(variable=self.v6)
        self.Radiobutton2_04.configure(value=0.0005)


        self.Radiobutton2_50 = tk.Radiobutton(self.Labelframe1_20)
        self.Radiobutton2_50.place(relx=0.074, rely=0.569, relheight=0.163
                , relwidth=0.491, bordermode='ignore')
        self.Radiobutton2_50.configure(activebackground="#ececec")
        self.Radiobutton2_50.configure(activeforeground="#000000")
        self.Radiobutton2_50.configure(background="#d9d9d9")
        self.Radiobutton2_50.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_50.configure(foreground="#000000")
        self.Radiobutton2_50.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_50.configure(highlightcolor="black")
        self.Radiobutton2_50.configure(justify='left')
        self.Radiobutton2_50.configure(text='0.3‰')
        self.Radiobutton2_50.configure(variable=self.v6)
        self.Radiobutton2_50.configure(value=0.0003)

        self.Radiobutton2_7 = tk.Radiobutton(self.Labelframe1_20)
        self.Radiobutton2_7.place(relx=0.546, rely=0.569, relheight=0.171
                , relwidth=0.347, bordermode='ignore')
        self.Radiobutton2_7.configure(activebackground="#ececec")
        self.Radiobutton2_7.configure(activeforeground="#000000")
        self.Radiobutton2_7.configure(background="#d9d9d9")
        self.Radiobutton2_7.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2_7.configure(foreground="#000000")
        self.Radiobutton2_7.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2_7.configure(highlightcolor="black")
        self.Radiobutton2_7.configure(justify='left')
        self.Radiobutton2_7.configure(text='''不缴纳''')
        self.Radiobutton2_7.configure(variable=self.v6)
        self.Radiobutton2_7.configure(value=0)


#清空输出框
    def deletetext(self):
        self.Text1.delete("0.0", "end")

#清空输入框
    def deleteentry2(self):
        self.Entry1.delete(0, "end")
        self.Entry1.insert(0,'0')

        self.Entry1_3.delete(0, "end")
        self.Entry1_3.insert(0,'1')

        self.Entry1_4.delete(0, "end")
        self.Entry1_4.insert(0,'0')



if __name__ == '__main__':
    vp_start_gui()