from PIL import Image,ImageDraw
import math
import random
Directions = ["north", "south", "east", "west"]
Blue= (50, 147, 168)
Black = (0, 0, 0)
Red= (201, 26, 26)


def Generate(colour=Blue):
  width = 800
  height = 600
  img = Image.new('RGB', (width, height), color=Blue)
  img.save("original.png")

# Generate()
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
def squarepoints(rangenumber=1):
  global offsets
  global newoffsets
  offsets = []
  newoffsets = []

  for i in range(4):
    x = (random.randint(0 - rangenumber, rangenumber))
    y = (random.randint(0 - rangenumber, rangenumber))
    coord = (x,y)
    print(coord)
    offsets.append(coord)
    print(offsets)


coords = {
    "north": [],
    "south": [],
    "east": [],
    "west": []
    }

def MountainTetonicGeneration(IMAGE):
      img = Image.open(IMAGE)
      width, height = img.size
      cy = width // 2
      cx = height // 2
      centercords = (cx, cy)
      coords['north'].append((cx, cy))
      coords['south'].append((cx, cy))
      coords['east'].append((cx, cy))
      coords['west'].append((cx, cy))
      
      print(f"Center cords: {centercords}")
      global Directions
      Plateusisthere = random.randint(0, 1)
      for direction in Directions:
        for _ in range(3):
            if direction == "north":
              current =(random.randint(cx, cx + cx // 2), random.randint(cy, cy * 2))
              if current not in coords["north"]:
                coords["north"].append(current)
            elif direction == "south":
              current = (random.randint(cx, cx + cx // 2), random.randint(0, cy // 2))
              if current not in coords["south"]:
                coords["south"].append(current)
            elif direction == "east":
              current = random.randint(0,cx), random.randint (0, cy // 2)
              if current not in coords["east"]:
                coords["east"].append(current)            
            elif direction == "west":
               current = random.randint(cx, cx * 2), random.randint(cy, cy + cy // 2)
               if current not in coords["west"]:
                  coords["west"].append(current)
               
      makeline(coords["north"], img, "yes")
      makeline(coords["south"], img, "yes")
      makeline(coords["east"], img, "yes")
      makeline(coords["west"], img, "yes")

      print(f"Northern coords: {coords['north']}")
      print(f"Southern coords: {coords['south']}")
      print(f"Eastern coords: {coords['east']}")
      print(f"Western coords: {coords['west']}")
      img.save('output_with_line.png')
      img.show()


      # print(f"Northern cords: {northerncords} southern cords: {southerncords} eastern cords: {easterncords} western cords: {westerncords}")

                 
            
      
      
         
def makeline(values, img, colourroll="yes"):
    draw = ImageDraw.Draw(img)
    if colourroll == "yes":
        Plateusisthere = random.randint(0, 1)
    else:
        Plateusisthere = 0
    if Plateusisthere == 1:
        colour = Red
    else:
        colour = Blue

    draw.line(values, fill=colour, width=5)
    if Plateusisthere == 1:
      values.append(("Plateu", "true"))
    else:
      values.append(("mountain", "true"))

       

       

def MountainGeneration(IMAGE,coords):
    print("Generating mountains...")
    img = Image.open(IMAGE)
    for i in coords:
        print(coords[i])

    

