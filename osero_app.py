import tkinter
import random
from PIL import Image, ImageTk


cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
pl_t = 0

def mouse_move(e):#マウスの現在地
  global mouse_x,mouse_y
  mouse_x = e.x
  mouse_y = e.y

def mouse_press(e):#マウスクリック
  global mouse_c
  mouse_c = 1

osero = [
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,2,1,0,0,0],
  [0,0,0,1,2,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0]
]

def put_osero():#オセロの表示
  for y in range(8):
    for x in range(8):
      if osero[y][x] == 1:
        cvs.create_image(x*72+36,y*72+36,image=black,tag="OSERO")
      elif osero[y][x] == 2:
        cvs.create_image(x*72+36,y*72+36,image=white,tag="OSERO")


def game_main():
  global cursor_x,cursor_y,mouse_c,pl_t
  if mouse_x < 72*8 and mouse_y < 72*8:
    cursor_x = int(mouse_x/72)
    cursor_y = int(mouse_y/72)
    if mouse_c == 1:
      mouse_c = 0
      if pl_t == 0:
        osero[cursor_y][cursor_x] = 1
        pl_t = 1
      else:
        osero[cursor_y][cursor_x] = 2
        pl_t = 0
  
  cvs.delete("OSERO")
  put_osero()
  root.after(100,game_main)


root = tkinter.Tk()
root.title("普通のオセロ")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
cvs = tkinter.Canvas(root,width=576,height=576)
cvs.pack()

bg = ImageTk.PhotoImage(file="osero.png")
black = ImageTk.PhotoImage(file="osero_black.png")
white = ImageTk.PhotoImage(file="osero_white.png")

cvs.create_image(288,288,image=bg)
game_main()
root.mainloop()


