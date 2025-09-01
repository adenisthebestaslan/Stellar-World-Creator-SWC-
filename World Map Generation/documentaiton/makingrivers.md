# Creating Rivers:

## setting up our function
```
def createrivers(coords,IMAGE):
    img = Image.open(IMAGE)
    draw = ImageDraw.Draw(img)
    width, height = img.size


```
We set up 2 arguments. Coords and our image. We add our draw varible, and then grab our width and higth from the overall size.

## Setting Up The Inital Loop p1
```
    for i in coords.items():
        riverlist = []
        print(i)
        if ["mountain", "true"] in i[1]:
            print("approoved")
            
            ValidCoordsRivers= i[1].copy()
            ValidCoordsRivers.pop()
            print(f"...l...{ValidCoordsRivers}")
            print(i[1])
```
afterwards, we check each item in the coords: If these coords contain the ``["mountain", "true"]`` tag, then we print that we're using them.
we make a copy of the coords for THAT mountain, so that way we can edit them for later. We remove ``["mountain", "true"]`` tage before printing 
out coords two times, one with the tag and one without it.


## Setting Up The Inital Loop p2

```
            for itempoint in range(3):
                point = random.choice(ValidCoordsRivers)
                print(point)
                riverlist.append([point])
                print(f"point:{point}")
                addtooriverlist = []
```
We run this loop three times:(we will later run more code inside this loop) we set the starting point of our river to a random item in ```ValidCoordsRivers```
and print it. we append this point to a list called Riverlist, and we print it again, we make a new list called addtoriverlist = []
## appending a value
```
                for item in range(6):
                    print()
                    print("...")

                    newitem = ((riverlist[itempoint][-1][0] + random.randint(30,40),riverlist[itempoint][-1][1] + random.randint(30,40)+ 4))
                    print(newitem)
                    if newitem[0]  < width - 1  and  newitem[1] < height - 1:
                        if is_on_land(img, newitem[0], newitem[1]) == True:
                            addtooriverlist.append(tuple(newitem))
```

continuing the loop from last time, we make a new loop that runs 6 times: we print a check before making a tuple called new item. This new item is the last xitem 
of the river currently being  drawn + 30-40, as well as the last y integer doing the same exact thing. we printour new point before checking if their within the
bounds of the image. if so, then we check if their on land, before adding them to our list.
## drawing and adding
```
  if addtooriverlist:  # only add if non-empty
                    riverlist[itempoint].extend(addtooriverlist)
                    print(f"river lisyt{riverlist}")
                
            for i in riverlist:
                i = [tuple(pt) for pt in i]
                print(f"testing: {i}")
                draw.line(i, fill=Blue, width=3)
    
            
            # riverlist = [tuple(pt) for pt in riverlist]
            #  #checks if each item in riverlist is a tuple
            # draw.line(riverlist, fill=Blue, width=3)
            # riverdata[i[0]] = riverlist



    print(f"riverlist: {riverdata}")
    img.save('rivers.png')
    img.show()

```

if add to riverlist exists, then we extend it with our new river. we print our final river before  converting and 
drawing each point. we then print our data a gain and save our pictuere, as well as draw it.
