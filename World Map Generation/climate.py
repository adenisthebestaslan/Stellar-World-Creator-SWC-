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

directions = ["east", "west", "north", "south"]
def createwind(IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    cx = width // 2
    cy = height // 2
    
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


    print(windmappoints)

    linecoords = [((1,windmappoints["point1"][0]),(width - 1,windmappoints["point1"][0])),((1,windmappoints["point2"][0]),(width - 1,windmappoints["point2"][0])),]
    print(linecoords)
    draw.line(linecoords[0], fill=Red, width=3)
    draw.line(linecoords[1], fill=Red, width=3)
    font = ImageFont.load_default()
    draw.text((0, windmappoints["point1"][0]), str(windmappoints["point1"]), fill=Blue, font=font)
    draw.text((0, (windmappoints["point1"][0] + windmappoints["inbetween"][0] // 2)), str(windmappoints["inbetween"]), fill=Blue, font=font)
    draw.text((0, windmappoints["point2"][0]), str(windmappoints["point2"]), fill=Blue, font=font)
    

    img.save('windmap.png')
    img.show()
    #(::( Jerry recently picked up a job gaurding this show function. Its his first Summer Job! Wish Him Luck

riverdata = {
}
# def createrivers(coords, riverdata):
#     for i in coords.items():
#         print(i)
#         riveroptions = [item for item in i if isinstance(item, tuple) and all(isinstance(n, (int, float)) for n in item)]
#         if ["mountain", "true"] in i:
#             riverdata[f"river{i[0]}"] = random.choice(riveroptions)[1] + 20
#             print(riverdata)
            




# createrivers(coords, riverdata)
