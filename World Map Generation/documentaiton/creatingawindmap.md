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

We import
