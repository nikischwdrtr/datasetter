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

# create new folder
if os.path.isdir(directoryNo):
  pass
else:
  newpathNo = os.path.join(path, directoryNo)
  os.mkdir(newpathNo)
if os.path.isdir(directoryYes):
  pass
else:
  newpathYes = os.path.join(path, directoryYes)
  os.mkdir(newpathYes)

# get images
for filename in os.listdir(path):
  if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".JPG") or filename.endswith(".JPEG") or filename.endswith(".PNG") or filename.endswith(".WEBP"):
    getImages.append(filename)
  else:
    continue

#tk settings for display image
root = Tk()
root.configure(bg='black')
canvas = Canvas(root, width=1024, height=1024, bg='black', highlightthickness=0)
canvas.pack() 

#load images
img = []
pixelsx = []
pixelsy = []
tkimg = []
for x in range(len(getImages)):
  img.append(x)
  tkimg.append(x)
  pixelsx.append(x)
  pixelsy.append(x)
for x in range(len(getImages)):
  img[x] = Image.open(getImages[x])
  if img[x].size[0] > img[x].size[1]: 
    pixelsx[x], pixelsy[x] = tuple([int(1024/img[x].size[0] * z)  for z in img[x].size])
  else: 
    pixelsx[x], pixelsy[x] = tuple([int(1024/img[x].size[1] * z)  for z in img[x].size])
  tkimg[x] = ImageTk.PhotoImage(img[x].resize((pixelsx[x], pixelsy[x])))  

#next image and decision functions
imgNumber = IntVar(root, value = 0)
def leftKey(event):
  decision.append(0)
  moveImages(imgNumber.get())
  imgNumber.set(imgNumber.get()+1)
  canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])
def rightKey(event):
  decision.append(1)
  moveImages(imgNumber.get())
  imgNumber.set(imgNumber.get()+1)
  canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])

#move images function
def moveImages(x):
  if decision[x] == 0:
    shutil.move(getImages[x], './no/'+getImages[x])
  elif decision[x] == 1:
    shutil.move(getImages[x], './yes/'+getImages[x])
  if len(decision) == len(getImages):
    root.destroy()

#key bindings
root.bind('<Left>', leftKey) 
root.bind('<Right>', rightKey) 
 
#load images
imgcontainer = canvas.create_image(512, 512, anchor=CENTER, image=tkimg[imgNumber.get()]) 
root.mainloop() 
