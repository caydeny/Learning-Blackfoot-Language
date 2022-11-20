# Your header
import cmpt120image

def isBlack(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return r < 100 and g < 100 and b < 100

def recolorImage(img,color):
  imgHeight = len(img)
  imgWidth = len(img[0])  
  canvas = cmpt120image.getWhiteImage(imgHeight, imgWidth)
  imgHeight = len(img)
  imgWidth = len(img[0]) 
  for row in range(imgHeight):
    for col in range(imgWidth):
      if isBlack(img[row][col]):
        canvas[row][col] = color

  #return canvas
  cmpt120image.showImage(canvas)
  
def minify(img):
  imgHeight = len(img)
  imgWidth = len(img[0])
  x = (imgHeight/2)
  y = (imgWidth/2)
  canvas = cmpt120image.getBlackImage(int(x),int(y))
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
      canvas[int(row/2)][int(col/2)] = list
  return canvas
  #cmpt120image.showImage(canvas)



def mirror(img):
  imgHeight = len(img)
  width = len(img[0])   
  canvas = cmpt120image.getBlackImage(imgHeight,width)
  for row in range(imgHeight): 
    counter = 0
    for col in range(width-1, -1, -1):
      canvas[row][counter] = (img[row][col])
      counter += 1
  return canvas
  #cmpt120image.showImage(canvas)
 
def drawItem(img,row,col):
  canvas = cmpt120image.getWhiteImage(400, 300)
  imgHeight = len(img)
  imgWidth = len(img[0]) 
  canvas[row][col] = img[0][0]
  for i in range(imgHeight):
    for j in range(imgWidth):
      if isBlack(img[i][j]):
        canvas[row+i][col+j] = img[i][j]
  return canvas
  #cmpt120image.showImage(canvas)


#def distributeItems(canvas,item,n):
#   # Add your code here



img = cmpt120image.getImage("child.png")  
#img = cmpt120image.getImage("apples.png")
#minify(img)
#recolorImage(img,[255,0,0])
#mirror(img)
drawItem(img, 100, 0)
input()
