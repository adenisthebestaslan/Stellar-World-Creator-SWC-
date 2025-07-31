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
 ```
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
```
  
  
first, this defines a function, with radius, center, points between 5 and 5. it sets the center of the image as 100,100, before prinint the points that were defined at the begining of the function.
After this, we split the circle into parts based on pi * 2 / points. it prints the angles before proceeding to define pointslist.

Here is a quick explination of the arguments, if you need them: 
| Arugment | default| purpose |
|----------|:---------:|---------:|
|radius| 100|sets the radius, or distance from the centre of the circle to the outside of the circle|
|center| 100,100|sets the centre of the image.|
|points|5 to 15 | used to divide the circle, will later be multiplied with i to find the areas of the circle where the angles are|

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
  for every point defined in the arguments, we'll take our current angle and multiply it by the I. this allows us to determine our current point, before we make our iregularit. then, we take this iregularity and multiplyi t by the radius argument from earlier, where we add one and a number between the negitive of our irregularity and the positive of our iregularity. it then makes our x and y varibles by taking both values repectivley and adding R *cos/sin to make the x why coords
  ```
  draw.polygon(pointslist, fill='Black')
  image.save("my_blob.png")
  #saves the blob as a png
  print(pointslist)

generateBlob(radius=50, center=(100, 100),)`
```
it draws all the points inbetween our polygon and fills them, before saving the points as a points list
