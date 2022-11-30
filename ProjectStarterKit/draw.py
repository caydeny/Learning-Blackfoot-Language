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
 
def drawItem(canvas,item,r,c):
  height_item = len(item) # Rows
  width_item = len(item[0]) # Columns
  
  for row in range(0,height_item):
    for col in range(0,width_item):
      if item[row][col][0] < 230 or \
         item[row][col][1] < 230 or \
         item[row][col][2] < 230:   # V2: Test for non-white
        canvas[r+row][c+col] = item[row][col]
  return canvas

def distributeItems(canvas,item,n):
  height_canvas = len(canvas) 
  width_canvas = len(canvas[0])
  height_item = len(item)
  width_item = len(item[0])
  for i in range(n):
    r = random.randint(0,height_canvas-height_item)
    c = random.randint(0,width_canvas-width_item)
    canvas = drawItem(canvas,item,r,c)
  return canvas