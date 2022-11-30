# Draw.py
# Cayden Yoo and Clifton Tan
# November 23rd 2022

import cmpt120image
import random

def isBlack(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return r < 100 and g < 100 and b < 100

def recolorImage(img,color):
  imgHeight = len(img)
  imgWidth = len(img[0])  
  result = cmpt120image.getWhiteImage(imgHeight, imgWidth)
  imgHeight = len(img)
  imgWidth = len(img[0]) 
  for row in range(imgHeight):
    for col in range(imgWidth):
      if isBlack(img[row][col]):
        result[row][col] = color
  return result
  
def minify(img):
  imgHeight = len(img)
  imgWidth = len(img[0])
  x = (imgHeight/2)
  y = (imgWidth/2)
  result = cmpt120image.getBlackImage(int(x),int(y))
  for row in range(0, imgHeight, 2):
    for col in range(0, imgWidth, 2):
      r = 0
      g = 0
      b = 0
      for i in range(2):
        for j in range(2):
          r += img[row + i][col + j][0]
          g += img[row + i][col + j][1]
          b += img[row + i][col + j][2]
      r = r/4
      g = g/4
      b = b/4
      list = [r, g, b]
      result[int(row/2)][int(col/2)] = list
  return result

def mirror(img):
  imgHeight = len(img)
  width = len(img[0])   
  result = cmpt120image.getBlackImage(imgHeight,width)
  for row in range(imgHeight): 
    counter = 0
    for col in range(width-1, -1, -1):
      result[row][counter] = (img[row][col])
      counter += 1
  return result
 
def drawItem(canvas,item,row,col):
  imgHeight = len(item)
  imgWidth = len(item[0]) 
  canvas[row][col] = item[0][0]
  for i in range(imgHeight):
    for j in range(imgWidth):
      if isBlack(item[i][j]):
        canvas[row+i][col+j] = item[i][j]
  return canvas

def distributeItems(canvas,item,n):
  imgHeight = len(item)
  imgWidth = len(item[0])
  for i in range(n):
    xcoord = random.randint(0,300)
    ycoord = random.randint(0,400)
    canvas = drawItem(canvas,item,ycoord,xcoord)
  return canvas
