## the begining
```
veglist = []
def calctreesveg(precipation):
    treelevel = precipation * 3
    print(f"treelevel: {treelevel}")
    for category in tree.getroot():
       print(f"{category.tag.capitalize()}:")
    # Loop through all items inside each category
   
   ```
we define a list called "Veglist" that stores our plants. We set a varible called tree level that is simply our precpitation times 3. we print this you.
we check each plant in our tree before showing the name of the tag group capitalized

```
for plant in category:
           print(f"  {plant.tag}: {plant.text}")
           if int(plant.text) <= treelevel:
               veglist.append(plant.tag)
               print(f"added {plant.tag} to veglist") 
    print(f"veggies: {veglist}")
    return veglist
```
for each plant in one of these groups, we print our tag and text, and check if the plants tree number is greater than Treelevel,
if so, we appened the tag to our veglist and print that we added it. we print our veggies afterwards and return them.
