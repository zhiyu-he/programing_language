# -*- coding: utf-8 -*-

from tkinter import *
root = Tk()

w = Canvas(root, width=600, height=800, background="white")
w.pack()

# head, x1, y1, x2, y2
w.create_oval(150, 100, 450, 400, outline="black", fill="#0094F0")

# face
w.create_oval(175, 150, 425, 400, outline="black", fill="#FFFFFF")

# eyes, y1, y2不变,移动的是x
w.create_oval(250, 115, 300, 180, outline="black", fill="#FFFFFF")
w.create_oval(300, 115, 350, 180, outline="black", fill="#FFFFFF")

w.create_oval(280, 137, 295, 159, outline="black", fill="#000000")
w.create_oval(305, 137, 320, 159, outline="black", fill="#000000")

w.create_line(287.5, 145, 287.5, 151, fill='white', width=3, capstyle='round')
w.create_line(312.5, 145, 312.5, 151, fill='white', width=3, capstyle='round')

w.create_line(300, 180, 300, 300, fill='#000000', width=1)


w.create_line(200, 240, 280, 240, fill='#000000', width=1.5)
w.create_line(320, 240, 400, 240, fill='#000000', width=1.5)

w.create_line(210, 280, 280, 260, fill='#000000', width=1.5)
w.create_line(320, 260, 390, 280, fill='#000000', width=1.5)

w.create_line(210, 200, 280, 220, fill='#000000', width=1.5)
w.create_line(320, 220, 390, 200, fill='#000000', width=1.5)

# mouse
w.create_arc(175, 50, 425, 300, width=1, style=ARC, start=240, extent=60)

# nose
w.create_oval(290, 170, 310, 190, outline="black", fill="#FF1900")


w.create_arc(-75, 325, 265, 665, width=1, start=35, extent=20, style=PIESLICE, outline='black', fill='#0094F0')
w.create_arc(335, 325, 675, 665, width=1, start=125, extent=20, style=PIESLICE, outline='black', fill='#0094F0')


w.create_arc(50, 450, 140, 540, width=1, start=35, extent=20, style=PIESLICE, outline='white', fill='#FFFFFF')
w.create_arc(460, 450, 550, 540, width=1, start=125, extent=20, style=PIESLICE, outline='white', fill='#FFFFFF')


w.create_arc(50, 450, 140, 540, width=1, start=35, extent=20, style=PIESLICE, outline='white', fill='#FFFFFF')
w.create_arc(460, 450, 550, 540, width=1, start=125, extent=20, style=PIESLICE, outline='white', fill='#FFFFFF')

# hand
w.create_oval(120, 430, 160, 470, outline="black", fill="#FFFFFF")
w.create_oval(440, 430, 480, 470, outline="black", fill="#FFFFFF")


w.create_rectangle(188, 350, 412, 550, outline="black", fill="#0094F0")

w.create_oval(215, 340, 385, 510, outline="white", fill="#FFFFFF")
w.create_line(188, 350, 412, 350, width=15, capstyle='round', fill='#FF1900')

# 腹部
w.create_arc(240, 365, 360, 485, width=1, start=180, extent=180, style=PIESLICE, outline='black', fill='#FFFFFF')

# foot
w.create_arc(280, 530, 320, 570, width=1, start=0, extent=180, style=PIESLICE, outline='white', fill='#FFFFFF')

w.create_oval(170, 530, 290, 570, outline="black", fill="#FFFFFF")
w.create_oval(310, 530, 430, 570, outline="black", fill="#FFFFFF")

# 铃铛
w.create_oval(286, 346, 314, 374, outline="black", fill="#FFF000")
w.create_rectangle(286, 357, 314, 361, outline="black", fill="#FFF000")
w.create_oval(297, 363, 303, 369, outline="black", fill="#FF1900")
w.create_line(300, 369, 300, 374, width=1, fill="#000000")
"""

#铃铛部分，黄色
w.create_oval(286, 346,314,374,outline="black",fill="yellow")
#铃铛的横线，黄色,使用矩形

#铃铛上的小红圆
w.create_oval(297, 363,303,369,outline="black",fill="red")
#脸上的竖线黑色
w.create_line(300,369,300,374,fill='black',width=1)
"""
if __name__ == '__main__':
    root.mainloop()
