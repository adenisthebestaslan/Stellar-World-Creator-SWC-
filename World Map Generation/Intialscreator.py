from PIL import Image,ImageDraw
import math
import random

Blue= (50, 147, 168)
Black = (0, 0, 0)


def Generate(colour=Blue):
  width = 800
  height = 600
  img = Image.new('RGB', (width, height), color=Blue)
  img.save("original.png")

Generate()
#pi = 3.14, so 2pi/circumfrence= 6.28.
#i had to learn about radius for this!
#basically, the radius is the distance from the center to the edge of the blob.
def generateBlob(radius=100, center=(100, 100),points=random.randint(5, 15)):
  image = Image.new('RGBA', (200, 200), 'white')
  draw = ImageDraw.Draw(image)

  center = (100, 100)
  radius = 100
  # the radius of the circle
  print(f"Points: {points}")
  #hoe many points will be used to create the blob
  angles = 2 * math.pi / points
  print(f"angles: {angles}")
  #splits the circle into equal parts, a point for each part
  pointslist = []
  for i in range(points):
    angle = i * angles
    #the angles/parts of the circle is equal to the item x the angle\
    irregularity = random.uniform(0.5, 1)
    #irregularity is here to change the radius of the angle slightly
    r = radius * (1 + random.uniform(-irregularity, irregularity))
    #changes some of the radius to make the blob irregluar
    x = center[0] + r * math.cos(angle)
    y = center[1] + r * math.sin(angle)
    pointslist.append((x, y))
    
    #converts to x y coords
    print(f"Point {i}: {r} ({x}, {y})")
  draw.polygon(pointslist, fill='Black')
  image.save("my_blob.png")
  #saves the blob as a png
  print(pointslist)

generateBlob(radius=50, center=(100, 100),)