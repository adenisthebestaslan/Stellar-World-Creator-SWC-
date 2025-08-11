# mountains and Tetconics

## the begining
```

def is_on_land(img, x, y):
    try:
        pixel = img.getpixel((int(x), int(y)))
        return pixel == Black  # Land is black
    except IndexError:
        return False  
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

```
First thing, we define a function to check if a pixel is on land or not: we try seeing what colour the pixel is, and if that pixel is black, then we will return true. if not, we will return false.
we start by setting up our coords, north south east and west. this dictionaty will allow us to make the lines indivusaly and keep good track.
we'll then define the function MountainTetonicGeneration, with 1 argument(IMAGE), before using that argument to open a new image.
The width and hight of the image are kept track of, before both of them respectivley are divided by two in order to get our center. We add these
to a varible named centercoords before appending these coords to the north, south, east, and west parts of the dictonary.  

## recording the coords

```
      print(f"Center cords: {centercords}")
      global Directions
      Plateusisthere = random.randint(0, 1)
      for direction in Directions:
        for _ in range(3):
            if direction == "north":
              current =(random.randint(cx, cx + 30), random.randint(cy, height - 1))
              if current not in coords["north"] and is_on_land(img, current[0], current[1]) == True:
                coords["north"].append(current)
                print("hi")
            elif direction == "south":
              current = (random.randint(cx, cx + 30 ), random.randint(0, cy // 2))
              if current not in coords["south"] and is_on_land(img, current[0], current[1]) == True:
                coords["south"].append(current)
            elif direction == "east":
              current = random.randint(0,cx), random.randint (0, cy // 2)
              if current not in coords["east"] and is_on_land(img,current[0], current[1]) == True:
                coords["east"].append(current)            
            elif direction == "west":
               current = random.randint(cx,width - 1), random.randint(cy, cy + 30)
               if current not in coords["west"] and is_on_land(img, current[0], current[1]) == True:
                  coords["west"].append(current)
            
```

We print our center coords before making Directions global. We prevoisly defined this varible in the begiing of this script, for which the documentation can be found [here](URL "seeandblob.md"). 
for every item in direction, it assigns a random coord based on the direction listed. if this coord is in this list, it doenst assign it.
Here is a table to understand how it generates values.
| direction | x | y|
|----------|:---------:|---------:|
| north | inbetween CX and CX plus half of CX| CY and  height - 1|
| South | inbetween CX and CX plus half of CX   | Inbetween 0 and CY divided by 2  |
| east | inbetween 0 and CX| Inbetween 0 and CY divided by 2  |
| east | inbetween CX and width - 1| Inbetween 0 and CY divided by 2  |

After we assign these values, we check if these cordinates fit two criteria:
if they arent already in the coords and they arent touching water, we append them

## printign our image:
```
      
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
```
The code runs make line for all for coords before printing the, and saving the image. When the Makeline function is run, it has 3 arguments: values, img, and colourroll.
here is a quick explanation of all of them

| argument | defualt | purpouse|
|----------|:---------:|---------:|
| values | none| the points that will be drawn to make a line|
| img | none| the image in which the lines will be drawn ontop of|
| colourroll| "yes"| checks if the colour will be rolled to create diffrent coloured barriers that will then be used in mountain generation to decide the placement of mountains.|

It will make Plateausisthere 0 at the begining to avoid confusion about varible names if the user sets colourroll to 0.
it will set the draw varible so we can draw on the image bedore checking if colourroll = yes. if it does, it rolls between 1 and 0 to see if the line will become red to for plateus. If not, it will simply not collour rhe lines. If Plateausisthere = 1:, it'll set the colour of that line to red. if it isnt, itll set it to blue. Itll then draw these lines by connecting the points and fillinf them with the coulour that was chosen earlier.
finaly, it adds data based on plateus. If Plateusisthere = 1, itll set the end to Plateu, True. if its 0, itll set it to "Mountain, true"

```
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
```
we then define mountain generation by setting two arguments: heres a table to understand them
| argument | defualt | purpouse|
|----------|:---------:|---------:|
| IMAGE | none| the image we'll be drawing on| 
|coords| none | the coords form earlier, which will be used  to make a line around the mountain.|

it prints "generating mountains..." to show its starting the scrip before mkaing a image. we make a deep coppy of the coords. for every item in the coords from earlier, we print them
for every item in courds, it prints it. If it contains the tag (Plateau Treu) it will remove the tag and make the lines thinner and darker, if not, it will also remove the tag and make them larger and  lighter. We then save the final product before showing it.


```
def savedata(coords):
      print("...................")
      filepath = "output.json"
      with open(filepath, "w") as json_file:
        json.dump(coords, json_file)
```
we create a function called savedata, and then add coords as a argument. We print a check before defining our filepath as "output.json"
we open filepath in write mode as a json file before dumping our coords.

```
MountainTetonicGeneration("my_blob.png")
savedata(coords)
MountainGeneration("my_blob.png", coords)
```
we run MTG,
Save DATA,
and Mountain Generation

