from PIL import Image,ImageDraw
import math
import random
import copy
import json
Directions = ["north", "south", "east", "west"]
Blue= (50, 147, 168)
Tan = (227, 168, 5)
Red= (201, 26, 26)
Grey = (146,150,147)
LightGrey = (185, 189, 186)


def Generate(colour=Blue):
  width = 800
  height = 600
  img = Image.new('RGB', (width, height), color=Blue)
  img.save("original.png")

def is_on_land(img, x, y):
  try:
    pixel = img.getpixel((int(x), int(y)))
    if pixel[:3] == Tan[:3]:
        print(f"Checked ({x}, {y}) = {pixel}")
        return True  # Land is TAN
    else:
      return False  
  except IndexError:
    return False  # Coordinates out of image bounds
    
    
# Generate()
#pi = 3.14, so 2pi/circumfrence= 6.28.
#i had to learn about radius for this!
#basically, the radius is the distance from the center to the edge of the blob.
def generateBlob(radius=100, center=(100, 100),points=random.randint(5, 15)):
  image = Image.new('RGB', (200, 200), 'white')
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
  draw.polygon(pointslist, fill=Tan)
  image.save("my_blob.png")
  #saves the blob as a png
  print(pointslist)



coords = {
    "north": [(100,100)],
    "south": [(100,100)],
    "east": [(100,100)],
    "west": [(100,100)]
    }


def MountainTetonicGeneration(IMAGE):
      img = Image.open(IMAGE)
      width, height = img.size
      cx = width // 2
      cy = height // 2

      centercords = (cx, cy)
      coords['north'].append((cx, cy))
      coords['south'].append((cx, cy))
      coords['east'].append((cx, cy))
      coords['west'].append((cx, cy))
      
      print(f"Center cords: {centercords}")
      global Directions
      Plateusisthere = random.randint(0, 1)
      directionchecks = {
      "north": {"x": (cx, cx + 30), "y": (cy, height - 1)},
      "south": {"x": (cx, cx + 30), "y": (0, cy // 2)},
      "east":  {"x": (0, cx), "y": (0, cy // 2)},
      "west":  {"x": (cx, width - 1), "y": (cy, cy + 30)}
      }
      for direction in Directions:

        for _ in range(3):
            xr = directionchecks[direction]["x"]
            yr = directionchecks[direction]["y"]
            current = (random.randint(*xr), random.randint(*yr))
            if current not in coords[direction] and is_on_land(img, current[0], current[1]):
              coords[direction].append(current)
            print(f"Added {current} to {direction}")

            
               
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
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    print("Generating mountains...")
    coordsforgen = copy.deepcopy(coords)
    for i in coordsforgen:
        print(coordsforgen[i])
        # checkcoordsforwater(coords[i],img)
        if ("Plateu","true") in coordsforgen[i]:
          coordsforgen[i].remove(("Plateu","true"))
          coordstodraw = coordsforgen[i]
          print(coordstodraw)
          draw.line(coordstodraw, fill=Grey, width=3)
        elif ("mountain","true") in coordsforgen[i]:
           coordsforgen[i].remove(("mountain","true"))
           coordstodraw = coordsforgen[i]
           print(coordstodraw)
           draw.line(coordstodraw, fill=LightGrey, width=3)
    img.save('finalmountains.png')
    img.show()
        

print(coords)      
def savedata(coords,name):
      print("...................")
      filepath = (f"{name}")
      with open(filepath, "w") as json_file:
        json.dump(coords, json_file)


if __name__ == "__main__":
    generateBlob(radius=50, center=(100, 100),)
    MountainTetonicGeneration("my_blob.png")
    savedata(coords,"output.json")
    MountainGeneration("my_blob.png", coords)
