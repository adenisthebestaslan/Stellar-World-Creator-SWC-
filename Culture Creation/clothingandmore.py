#I realized that in order to decide a large portion of things, we need to be able to find what animals are in the area.
import xml.etree.ElementTree as ET
import random
def findanimals(precipitaiton,plants,tree,animallist):
    treelevel = precipitaiton * 3
    print(f"treelevel: {treelevel}")
    for category in tree.getroot():
       print(f"{category.tag.capitalize()}:")
       for animal in category:
           print(f"{animal.tag}: {animal.text}")
           result = animal.split(",")
           if int(result[0]) < treelevel and result[1] in plants:
               animallist.append(animal.tag)
               print(f"added {animal.tag} to veglist") 
    return animallist


def clothing(temprature,plants,animals):
    material = ''
    layers = max(1, round(5 - (temprature[1] / 20)))
    print(layers)
    if temprature[1] >= 60 and "flax" in plants:
        #since the climates precipitation would have to be wet inorder to grow flax anyways.
        material = "linen"

    elif temprature[1] >=60 and "sheep" in animals:
        material = "wool"


    
    if temprature[1] <= 45 and "cow" in animals:
            material = "Leather"
    elif temprature[1] <=45 and "sheep" in animals:
        material = "wool"
    
    designs = False
    roll = random.randint(1,10)
    chance = random.randint(1,10)
    if roll < chance:
        designs = True
    
    print(material, layers, designs)



clothing([52.5, 60.5],["thyme", "rosemarry", "dill", "daisies", "tulips", "sunflowers", "oak", "pine","cilantro","wheat","ants","lenin"],['cows','sheep'])
