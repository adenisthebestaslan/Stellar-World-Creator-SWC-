# creatingawindmap

```
import json
import random
import PIL
from PIL import Image, ImageDraw, ImageFont
Red= (201, 26, 26)
Blue= (50, 147, 168)

with open("output.json", 'r', encoding='utf-8') as f:
    json1 = f.read()  # read file content as a string
print(json1)
coords = json.loads(json1)  
print(coords)

windmappoints = {"point1" : [],
                 "inbetween" : [],
                 "point2": []
}

```

We import json before importing random and PIL. from PIL we import IMAGE, IMAGEDRAW, And Image font.
We define the colours Red and Blue.

we open the output file from earlier and we save it as json1. We make a dict called coords using json1 and print it. 
We define a  dictonary called windmap points which will later be used to divide the 


```
directions = ["east", "west", "north", "south"]
def createwind(IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    cx = width // 2
    cy = height // 2
```

we set up directions, before defining createwind with a argument for the image,
we set up draw before gettning the size form the immage. the center will be half of x and y respectivly

```
    windmappoints["point1"].append(random.randint(1,cy))
    windmappoints["point1"].append(random.choice(directions))
    winter1 = (w := random.randint(1, 8), random.randint(w, 17))

    print(f"winter:{winter1}")
    windmappoints["point1"].append(((winter1),((winter1[0] * 9/5) + 32),((winter1[1] * 9/5) + 32))) # (1, 2)
    
    print(windmappoints)
    
    winter2 = (w := random.randint(35, 46), random.randint(w, 60))
    windmappoints["point2"].append(random.randint(windmappoints["point1"][0]+15,height))
    windmappoints["point2"].append(random.choice(directions))
    windmappoints["point2"].append(((winter2),((winter2[0] * 9/5) + 32),((winter2[1] * 9/5) + 32))) # (1, 2)
    
    winter3 = (w := random.randint(17, 30), random.randint(w, 35))
    windmappoints["inbetween"].append((windmappoints["point2"][0]-windmappoints["point1"][0]))
    windmappoints["inbetween"].append(random.choice(directions))
    windmappoints["inbetween"].append(((winter3),((winter3[0] * 9/5) + 32),((winter3[1] * 9/5) + 32))) # (1, 2)
```
for each windmappoint we append a couple of stats.
here is a table explaining it
the area is defined with a point and a tempreature, as well as a direction, but that doesnt have any special rules
| area | point | tempretire|
|----------|:---------:|---------:|
| 1 | 1 to center width|1 - 17 C|
| 2 | none| the image in which the lines will be drawn ontop of|
| colourroll| "yes"| checks if the colour will be rolled to create diffrent coloured barriers that will then be used in mountain generation to decide the placement of mountains.|



