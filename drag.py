from tkinter import *  
from tkinter import ttk
from PIL import ImageTk,Image
import os, shutil

# path shizzle
path = "./"
directoryNo = "no"
directoryYes = "yes"
getImages = []
decision = []

#tk settings
root = Tk()
root.configure(bg='lightgrey')
canvas = Canvas(root, width=1050, height=1050, bg='lightgrey', highlightthickness=0)
canvas.pack() 

#resize and laod images
img = Image.open('./te.png')
if img.size[0] > img.size[1]: 
  pixelsx, pixelsy = tuple([int(1024/img.size[0] * z)  for z in img.size])
else: 
  pixelsx, pixelsy = tuple([int(1024/img.size[1] * z)  for z in img.size])
tkimg = ImageTk.PhotoImage(img.resize((pixelsx, pixelsy))) 

def rightKey(event):
  cropImage()

#img crop function
def cropImage():
  imgOGW = img.size[0]
  imgOGH =  img.size[1]
  imgX = canvas.coords(imgcontainer)[0]
  imgY = canvas.coords(imgcontainer)[1]
  imgW = tkimg.width()
  imgH = tkimg.height()
  imgXC = imgX-imgW/2
  imgYC = imgY-imgH/2
  imgDW = (imgW-imgOGW)/imgW*-1
  imgDH = (imgH-imgOGH)/imgH*-1
  left = 26-imgXC
  top = 26-imgYC
  right = imgXC+imgW-26
  bottom = imgYC+imgH-26
  leftD = int(left+left*imgDW)
  topD = int(top+top*imgDH)
  rightD = int(right+right*imgDW)
  bottomD = int(bottom+bottom*imgDH)
  imgC = img.crop((int(leftD),int(topD),int(rightD),int(bottomD)))
  imgC = imgC.resize((1024,1024))
  imgC.save("test.png")

#key bindings
root.bind('<Right>', rightKey) 
 
#show tkinter stuff
imgcontainer = canvas.create_image(525, 525, anchor=CENTER, image=tkimg)
canvas.create_rectangle(26, 26, 1024, 1024, fill='', outline ='#00FF00', width=2)
root.mainloop() 
