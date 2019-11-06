#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time : 2019/11/6 21:54
 @Author : Jason.Jia
 @contact: jiajunp@163.com
 @Version : 1.0
 @file :login.py
 @desc :
 
'''

from tkinter import  *
import  pymysql


#创建根窗口，并添加组件

def create_root():
    root = Tk()
    root.title('登录')
    root.resizable(0,0) #设置窗口大小不可改变
    canvas = Canvas(root) #添加画布

    canvas.pack(side ='top',fill=BOTH)
    canvas.create_window(100,50,window=Label(root, font=('宋体', 10), text='用户名', justify='left', padx=5, pady=4))  # 其中100,50为相对于画布的偏移量，左上角为0,0

    canvas.create_window(100,90,
                         window=Label(root, font=('宋体', 10), text='用户名', justify='left', padx=5, pady=4))

    #账号密码输入框

    zh_entry = Entry(root,borderwidth=3)
    password_entry = Entry(root,borderwidth=3,show='*')
    canvas.create_window(210,50,window=zh_entry)
    canvas.create_window(210,90,window=password_entry)
    canvas.create_window(330,90,window=Label(root, text='忘记密码', fg='red', font=('宋体', 10)))

    #创建画布背景图

    photo = PhotoImage(file='E:\\python\\Jason\\image\\1.jpg')
    canvas.create_image(200,150,image=photo)


    #button点击事件

    def callback():
        user = int(zh_entry.get())
        password = int(password_entry.get())
        user_information = sql_information('select * from user_information')

        if user == user_information[0][0] and password == user_information[0][1]:
            student_information = sql_information('select * from student_information')
            root.state('iconic') ## 隐藏窗口，相当于窗口最小化
            new_root(student_information)
        else:
            pass

    canvas.create_window(190, 200, window=Button(root, width=15, command=callback, bg='#87CEEB', text='立即登录'))
    mainloop()

def new_root(student_information):
    student_root = Toplevel()
    student_root.title("学生管理系统")
    student_root.resizable(0,0)
    head_string = ('学号', '姓名', '年级', '年龄', '家庭住址')
    for i in range(len(student_information[0])):
        listbox = Listbox(student_root, width=20, height=20, bd=4, relief='flat', bg='#E0FFFF')
        listbox.pack(side=LEFT, fill=BOTH)
        listbox.insert(END, head_string[i])
        for each in student_information:
            listbox.insert(END, each[i])


#进行数据连接，传入sql语句，返回需要的信息
def sql_information(sql):
    connection = pymysql.connect('localhost','root','root',"tang_crawler")
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        user_information = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if connection:
            cursor.close()
        if cursor :
            connection.close()
    return user_information


if __name__ == '__main__':
    create_root()