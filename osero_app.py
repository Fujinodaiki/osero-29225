import tkinter
import random
from PIL import Image, ImageTk


cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
mouse_lc = 0
pl_t = 0

def mouse_move(e):#マウスの現在地
  global mouse_x,mouse_y
  mouse_x = e.x
  mouse_y = e.y

def mouse_press(e):#マウスクリック左クリック
  global mouse_c
  mouse_c = 1

def mouse_right(e):
  global mouse_lc
  mouse_lc = 1

osero = [
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0],
  [0,0,0,0,2,0,0,0],
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
  global cursor_x,cursor_y,mouse_c,mouse_lc,pl_t
  if mouse_x < 72*8 and mouse_y < 72*8:
    fnt = ("Times New Roman",30)
    txt = "mouse({},{}){}{}".format(mouse_x,mouse_y,mouse_c,mouse_lc)
    txt1 = "mouse({},{})".format(cursor_x,cursor_y)
    cvs.delete("TEST")
    cvs.create_text(250,288, text=txt,fill="black",font=fnt,tag="TEST")
    cvs.create_text(200,318, text=txt1,fill="black",font=fnt,tag="TEST")
    cursor_x = int(mouse_x/72)
    cursor_y = int(mouse_y/72)
    if mouse_c == 1 and mouse_lc == 0:
      mouse_c = 0
      if pl_t == 0:     
            osero[cursor_y][cursor_x] = 1
          pl_t = 1
      else:
        osero[cursor_y][cursor_x] = 2
        pl_t = 0
    elif mouse_c == 0 and mouse_lc == 1:
      mouse_lc = 0
      osero[cursor_y][cursor_x] = 0
  
  cvs.delete("OSERO")
  put_osero()
  root.after(100,game_main)


root = tkinter.Tk()
root.title("普通のオセロ")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<Button-1>",mouse_press)
root.bind("<Button-2>",mouse_right)
cvs = tkinter.Canvas(root,width=576,height=576)
cvs.pack()

bg = ImageTk.PhotoImage(file="osero.png")
black = ImageTk.PhotoImage(file="osero_black.png")
white = ImageTk.PhotoImage(file="osero_white.png")

cvs.create_image(288,288,image=bg)
game_main()
root.mainloop()


