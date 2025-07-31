# mountains and Tetconics

## the begining
```
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
```

We print our center coords before making Directions global. We prevoisly defined this varible in the begiing of this script, for which the documentation can be found [here](URL "seeandblob.md").
for every item in direction, it assigns a random coord based on the direction listed. if this coord is in this list, it doenst assign it.
Here is a table to understand how it generates values
| direction | x | y|
|----------|:---------:|---------:|
| north | inbetween CX and CX plus half of CX| CY and CY times 2  |
| South | inbetween CX and CX plus half of CX   | Inbetween 0 and CY divided by 2  |
| east | inbetween 0 and CX| Inbetween 0 and CY divided by 2  |
| east | inbetween CX and CX times 2| Inbetween 0 and CY divided by 2  |



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
