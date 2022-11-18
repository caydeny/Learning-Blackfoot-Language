# Your header
import cmpt120image

def recolorImage(img,color):
  height = len(img)
  width = len(img[0])  
  canvas = cmpt120image.getBlackImage(height,width)
  def iswhite(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return r == 255  and g == 255 and b == 255
  height = len(img)
  width = len(img[0]) 
  for row in range(height):
    for col in range(width):
      if iswhite(img[row][col]):
        canvas[row][col] = img[row][col]
      else:
        canvas[row][col] = color
  return canvas

def minify(img):
  height = len(img)
  width = len(img[0])
  x = (height/2)
  y = (width/2)
  canvas = cmpt120image.getBlackImage(int(x),int(y))
  for row in range(0,height,2):
    for col in range(0,width,2):
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
      canvas[int(row/2)][int(col/2)] = list
  return canvas



def mirror(img):
  height = len(img)
  width = len(img[0])   
  canvas = cmpt120image.getBlackImage(height,width)
  for row in range(height): 
    counter = 0
    for col in range(width-1, -1, -1):
      canvas[row][counter] = (img[row][col])
      counter += 1
  return canvas
  
# def drawItem(img,item,row,col):
#   # Add your code here
  
#def distributeItems(img,item,n):
#   # Add your code here

img = cmpt120image.getImage("apples.png")
minify(img)
recolorImage(img,[255,0,0])
mirror(img)

