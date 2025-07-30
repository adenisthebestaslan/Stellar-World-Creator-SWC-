# Generating the sea:

## begining
`from PIL import Image,ImageDraw
import math
import random
Directions = ["north", "south", "east", "west"]
Blue= (50, 147, 168)
Black = (0, 0, 0)
Red= (201, 26, 26)`

first, we import PIL, before using Math and random.
we define some universal dirrections before setting up colors

## making the sea
`def Generate(colour=Blue):
  width = 800
  height = 600
  img = Image.new('RGB', (width, height), color=Blue)
  img.save("original.png")`
generates a full backgrund using BLUE from earlier, and proceeds to set the width and height. It makes a new RGB image with the width and height discribed, and saves it as a  png


# making the land:
## begining
`def generateBlob(radius=100, center=(100, 100),points=random.randint(5, 15)):
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
  pointslist = []`
  first, this defines a function, with radius, center, points between 5 and 5. it sets the center of the image as 100,100, before prinint the points that were defined at the begining of the function.
  After this, we split the circle into parts based on pi * 2 / points. it prints the angles before proceeding to define pointslist.

  
