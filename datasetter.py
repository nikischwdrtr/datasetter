from tkinter import *  
from tkinter import ttk
from PIL import ImageTk,Image
import os, shutil, math

print (" ")
print (" ______________________________________________________")
print ("|    ___  ___ _________   ___________________________  |")
print ("|   / _ \/ _ /_  __/ _ | / __/ __/_  __/_  __/ __/ _ \ |")
print ("|  / // / __ |/ / / __ |_\ \/ _/  / /   / / / _// , _/ |")
print ("| /____/_/ |_/_/ /_/ |_/___/___/ /_/   /_/ /___/_/|_|  |")
print ("|______________________________________________________|")
print ("|                                                      |")
print ("| datasetter.py v0.2 2022                              |")
print ("| \ \ tool for creating datasets                       |")
print ("|                                                      |")
print ("|______________________________________________________|")
print ("|                                                      |")
print ("|           dev@niklausiff.ch                          |")
print ("|           https://www.niklausiff.rip                 |")
print ("|______________________________________________________|")
print (" ")

print (">>> 0/2 settings")
print ("_______________________________________________________")

# input settings
print (" ")
print ("do you want to crop images? (y/n)")
while True:
  try:
    cropYN = input("> value: ")
    if not (cropYN == "y" or cropYN == "n"):
      raise ValueError
    break
  except ValueError:
    print (" ")
    print('>>ERROR')
    print('invalid input')
    print('must be y or n')
    print (" ")
if cropYN == "y":
  print (" ")
  print ("crop width (max 1024)")
  while True:
    try:
      cropWidth = int(input("> value: "))
      if cropWidth < 1 or cropWidth > 1024:
        raise ValueError
      break
    except ValueError:
      print (" ")
      print('>>ERROR')
      print('invalid input')
      print('must be range 1-1024')
      print (" ")
if cropYN == "y":
  print (" ")
  print ("crop height (max 1024)")
  while True:
    try:
      cropHeight = int(input("> value: "))
      if cropHeight < 1 or cropHeight > 1024:
        raise ValueError
      break
    except ValueError:
      print (" ")
      print('>>ERROR')
      print('invalid input')
      print('must be range 1-1024')
      print (" ")

print ("_______________________________________________________")
print (" ")
print (">>> 1/2 create folder // load images")
print ("_______________________________________________________")

# path shizzle
path = "./"
directoryNo = "no"
directoryYes = "yes"
directoryOG = "og"
directoryS = "sort"
directoryC = "crop"
getImages = []
getImagesM = []
decision = []
cropHowMany = []
crops = []
imgX = 1024/2
imgY = 1024/2
mouseX = 0
mouseY = 0

# create new folder
if os.path.isdir(directoryOG):
  pass
else:
  newpathOG = os.path.join(path, directoryOG)
  os.mkdir(newpathOG)
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
if os.path.isdir(directoryS):
  for filename in os.listdir(path+'/crop'):
    crops.append(1)
  cropName = len(crops)
else:
  cropName = 0
  newpathS = os.path.join(path, directoryS)
  os.mkdir(newpathS)
if os.path.isdir(directoryC):
  pass
else:
  newpathC = os.path.join(path, directoryC)
  os.mkdir(newpathC)

#get images for move/copy
for filename in os.listdir(path):
  if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".JPG") or filename.endswith(".JPEG") or filename.endswith(".PNG") or filename.endswith(".WEBP"):
    getImagesM.append(filename)
  else:
    continue

#move/copy images
for x in range(len(getImagesM)):
  shutil.copy('./'+getImagesM[x], './sort/'+getImagesM[x])
  shutil.move(getImagesM[x], './og/'+getImagesM[x])

#get images for sorting
for filename in os.listdir(path+'/sort/'):
  if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".JPG") or filename.endswith(".JPEG") or filename.endswith(".PNG") or filename.endswith(".WEBP"):
    getImages.append(filename)
  else:
    continue

#tk settings
root = Tk()
root.title('datasetter')
root.configure(bg='lightgrey')
canvas = Canvas(root, width=1050, height=1050, bg='lightgrey', highlightthickness=0)
if cropYN == "y":
  offsetX = 1050/2-cropWidth/2
  offsetY = 1050/2-cropHeight/2
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
  img[x] = Image.open('./sort/'+getImages[x])
  if img[x].size[0] > img[x].size[1]: 
    pixelsx[x], pixelsy[x] = tuple([int(1050-1050*0.08/img[x].size[0] * z)  for z in img[x].size])
  else: 
    pixelsx[x], pixelsy[x] = tuple([int(1050-1050*0.08/img[x].size[1] * z)  for z in img[x].size])
  tkimg[x] = ImageTk.PhotoImage(img[x].resize((pixelsx[x], pixelsy[x])))  

print ("_______________________________________________________")
print (" ")
print (">>> 2/2 gui for setting data")
print ("_______________________________________________________")

#next image/decision/crop functions
imgNumber = IntVar(root, value = 0)
def leftKey(event):
  decision.append(0)
  cropHowMany.append(1)
  moveImages(imgNumber.get())
def rightKey(event):
  decision.append(1)
  cropHowMany.append(1)
  moveImages(imgNumber.get())
def spaceKey(event):
  decision.append(1)
  cropHowMany.append(1)
  cropImage(imgNumber.get())
def wheel(event):
  resizeImage(event, imgNumber.get())
def moveTo(event):
  moveImage(event, imgNumber.get())

#move images function
def moveImages(x):
  if decision[x] == 0:
    shutil.move('./sort/'+getImages[x], './no/'+getImages[x])
  elif decision[x] == 1:
    shutil.move('./sort/'+getImages[x], './yes/'+getImages[x])
  if len(decision) == len(getImages):
    root.destroy()
  else:
    imgNumber.set(imgNumber.get()+1)
    canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])

#image crop function
def cropImage(x):
  global cropName
  imgOGW = img[x].size[0]
  imgOGH =  img[x].size[1]
  imgX = canvas.coords(imgcontainer)[0]
  imgY = canvas.coords(imgcontainer)[1]
  imgW = tkimg[x].width()
  imgH = tkimg[x].height()
  imgXC = imgX-imgW/2
  imgYC = imgY-imgH/2
  imgDW = (imgW-imgOGW)/imgW*-1
  imgDH = (imgH-imgOGH)/imgH*-1
  left = offsetX-imgXC
  top = offsetY-imgYC
  right = imgXC+imgW-offsetX
  bottom = imgYC+imgH-offsetY
  leftD = int(left+left*imgDW)
  topD = int(top+top*imgDH)
  rightD = int(right+right*imgDW)
  bottomD = int(bottom+bottom*imgDH)
  imgC = img[x].crop((leftD,topD,rightD,bottomD))
  imgC = imgC.resize((cropWidth,cropHeight))
  imgC = imgC.convert('RGB')
  imgC.save('./crop/'+str(cropName)+'.jpg')
  os.remove('./sort/'+getImages[x])
  cropName = cropName+1
  if len(cropHowMany) == len(getImages):
    root.destroy()
  else:
    imgNumber.set(imgNumber.get()+1)
    canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])

#resize image function
imgW = tkimg[x].width()
imgH = tkimg[x].height()
imgNW = imgW
imgNH = imgH
def resizeImage(event, x):
  global imgNW,imgNH
  if event.delta < 0:
    if imgNW-imgW*0.01 and imgNH-imgW*0.01 > 0:
      imgNW = int(imgNW-imgW*0.01)
      imgNH = int(imgNH-imgH*0.01)
    else:
      pass
    tkimg[x] = ImageTk.PhotoImage(img[x].resize((imgNW, imgNH)))
    canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])
  if event.delta > 0:
    if imgNW+imgW*0.01 and imgNH+imgW*0.01 < 4000:
      imgNW = int(imgNW+imgW*0.01)
      imgNH = int(imgNH+imgH*0.01)
    else:
      pass
    tkimg[x] = ImageTk.PhotoImage(img[x].resize((imgNW, imgNH)))
    canvas.itemconfig(imgcontainer, image=tkimg[imgNumber.get()])

#move image function
def moveImage(mouse,x):
  global imgX,imgY,imgcontainer,rect
  imgX = mouse.x
  imgY = mouse.y
  canvas.delete(imgcontainer,rect)
  imgcontainer = canvas.create_image(int(imgX), int(imgY), anchor=CENTER, image=tkimg[imgNumber.get()])
  if cropYN == "y":
    rect = canvas.create_rectangle(offsetX, offsetY, offsetX+cropWidth, offsetY+cropHeight, fill='', outline ='#00FF00', width=2)

#key bindings
root.bind('<Left>', leftKey) 
root.bind('<Right>', rightKey)
if cropYN == "y":
  root.bind("<space>", spaceKey)
root.bind("<MouseWheel>", wheel)
root.bind('<B1-Motion>', moveTo)
 
#load images // create crop frame
imgcontainer = canvas.create_image(imgX, imgY, anchor=CENTER, image=tkimg[imgNumber.get()])
if cropYN == "y":
  rect = canvas.create_rectangle(offsetX, offsetY, offsetX+cropWidth, offsetY+cropHeight, fill='', outline ='#00FF00', width=2)
root.mainloop()

print ("_______________________________________________________")
print (" ")
print (" ______________________________________________________")
print ("|                                                      |")
print ("| finished                                             |")
print ("|______________________________________________________|")
print ("|                                                      |")
print ("| original images:                                     |")
print ("| ./og                                                 |")
print ("| to be sorted images:                                 |")
print ("| ./sort                                               |")
print ("| yes or no images:                                    |")
print ("| ./yes  // ./no                                       |")
print ("| croped images:                                       |")
print ("| ./crop                                               |")
print ("|______________________________________________________|")
print ("|                                                      |")
print ("|           dev@niklausiff.ch                          |")
print ("|           https://www.niklausiff.rip                 |")
print ("|______________________________________________________|")
print (" ")