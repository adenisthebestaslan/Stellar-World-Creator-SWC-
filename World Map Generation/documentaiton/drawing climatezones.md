
```
import random
import Intialscreator 
import PIL
from PIL import Image, ImageDraw, ImageFont
import climate
import json
import os
```
we import our needed modules, including functions from initals and climates

## loading our json's and setting up a center generator:
```
coords = load_json("output.json")
riverlist = load_json("riverdata.json")
windmap = load_json("windmap.json")
```
we load our coords first, before defining this function:

```
def generatecent(blolb):
    
    while True:
        centcoords = (random.randint(0, 199), random.randint(0, 199))
        print(centcoords)
        if Intialscreator.is_on_land(blolb, centcoords[0], centcoords[1]):
            print("land!")
            return centcoords
            break
        else:
            print("...")
```
we take a image as a argument. We start a repeating loop where we generate centcoords, chosing 2 values between 199 and 1
we print these coords, and if they are on land, taking the arguments of the coord's x and y and the blob, we print that they're on land, and stop the loop.
if not, we keep going.

## checking our windzone
```
def checkwindzone(coord):
    print("checking")
    for i in windmap.keys():
        print(f"Processing windmap key: {i}")
        if coord[1] - 10 < windmap[i][0]:
            print(f"windzone is {i}")
            windzone = i
            break
        else:
            windzone = 'point2'
    return windzone
```
we set up a function called check windzone, using our coord as a argument.
for each item in the windmap's keys, we print to check before seeing if our x value - 10 is greater than our windmap's x.
if so, we say that our windzone is the key, and we break.
if not, we set it to point2.
we then return windzone
## normilizing coords
```
def nomralizecoords(protocoords,blob,center):
    finalcoords = []
    finalcoords.append((center[0]+10,center[1]))
    finalcoords.append((center[0]+20,center[1]+10))
    for i in protocoords:
        newcoord = []
        for item in range(len(i)):
            coordpos = i[item]
            if i[item] < 0:
                coordpos = (10)
            if i[item] > 200:
                coordpos = 190
            newcoord.append(coordpos)
        newcoord = tuple(newcoord)
        if Intialscreator.is_on_land(blob, newcoord[0], newcoord[1]):
            finalcoords.append(newcoord)
    return finalcoords
```
we set up a function with our original coords, our center, and our blob.
We then set up a list called finalcoords,  before appending 2 aditonal coords.
we check each proto coord, and create a list called newcoord on each iteration. we repeat a check for each item, using the length of the item to check. we make a varible called coordpos,
and if the item of that iteration is less than 0, we add a 10,
if its moree than 200, we set it to 190.
we append these, and turn them into tuples before checking if its onland. if it is, we append it to the final coords.
after the loop finishes, we return final coords.

## setting up climate details
```
def genclimatezone(length,blob,savefolderpath):
    
    coords = load_json("output.json")
    img = Image.open(blob)
    for item in range(length):
        generatecent(img)
        center = generatecent(img)
        centers.append(center)
    print(centers)
    for i in centers:
        name = input("what would you like to name this one?")
        os.mkdir(rf"{savefolderpath}\{name}")

        precipclimate = climate.preciptationgen(i,coords,riverlist)
        Intialscreator.savedata(precipclimate,rf"{savefolderpath}\{name}\precpitaion.json")
        veggies = climate.calctreesveg(precipclimate[0]+precipclimate[1])
        Intialscreator.savedata(veggies,rf"{savefolderpath}\{name}\veg.json")

        windzone = checkwindzone(i)
        print(windzone)
        windpoint = (windzone, windmap[windzone])
        climateitems = climate.climategen(windmap, windpoint, riverlist, coords)
        Intialscreator.savedata(climateitems,rf"{savefolderpath}\{name}\climates.json")
```
we set up a function called genclimatezone, setting up a argument for how much of the climates there will be, our imagepath, and the folder we want to save our climates too.
we repeat a loop the same number of times as length. In this loop, we generate centers and append it to a list called centers.
we finish with this loop before checking each item in center. We ask the user for the climates name and make a folder with that exact name, before generating Precipitation, veggitables, and
saving it. We then check our windzone and print it. We then set up our windpoint to be put in a climategen function,
and save that as well.

## generating coords to be normalized and drawing

```

        direction = climateitems[0]
        temp = climateitems[1]
        protocoords = [
        (i[0] + 60, i[1] + 30), 
        (i[0] - 30, i[1] + 60),
        (i[0] + 60, i[1] - 30),
        (i[0] - 30, i[1] - 60),
        ]
        finalcoords = nomralizecoords(protocoords,img,i)
        Intialscreator.savedata(finalcoords,rf"{savefolderpath}\{name}\coords.json")

        
        print(protocoords)
        print(finalcoords)

        t = 1 - ((precipclimate[0] + precipclimate[1] / 2) / 120)
        #divides our  precipitation average by our max, which is 120.
        r = int(210 * t)
        #we scale each
        g = int(255 + (180 - 255) * t)
        b = int((140 - 0) * t)
        draw = ImageDraw.Draw(img)
        colorgrad = (r,g,b)
        draw.polygon(finalcoords, fill=colorgrad)
    
    img.save('worldmap.png')
    img.show()
```
we set our direction to the first item of climate items, and our temp to the second.
We generate coords that are relivily close by, and put them thtough our normilize coords function.
We save our data before prinint both our protocoords and our finalcoords.
We then set a varible called t to 1 - our miniumum minus our maximium divided by 2 and divided by 120.
we then mutltiple r, g, and b by each of these values before setting up a draw varible, seting our coulours, and drawing our polygon.
We save our image and show it.


