"""
"""
from tkinter import * # จากpackage from tkinter ดึง ฟังชั่นมาทั้งหมด

GUI = Tk() #สร้างGUI ขึ้นมาละดึงฟังชั่นของ Tk() มาใช้
GUI.geometry('500x500')

L= Label(GUI,text='Hello World', font=(None, 30))
L.pack()
#Lable คือข้อความของโปรแรมเรา (L)
GUI.mainloop()