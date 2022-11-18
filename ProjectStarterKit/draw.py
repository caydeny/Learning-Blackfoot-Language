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
  canvas = cmpt120image.getBlackImage(height/2,width/2)
  
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
recolorImage(img,[255,0,0])
mirror(img)

