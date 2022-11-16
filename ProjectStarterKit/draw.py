# Your header
import cmpt120image

def recolorImage(img,color):
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
        pass
      else:
        img[row][col] = color
  cmpt120image.showImage(img)

def minify(img):
  height = len(img)
  width = len(img[0])

  
def mirror(img):
  
  cmpt120image.showImage(img)
  x = input()
  # output = cmpt120image.getBlackImage(80,80)
  # height = len(img)
  # width = len(img[0])
  # for coloumn in range(height):  
  #   for row in range(width, -1, -1):
  #     print(row)
  # cmpt120image.showImage(output)
  # x = input()
  

  
# def drawItem(img,item,row,col):
#   # Add your code here
  
#def distributeItems(img,item,n):
#   # Add your code here

img = cmpt120image.getImage("apples.png")
recolorImage(img,[255,0,0])
mirror(img)

