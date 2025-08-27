from PIL import Image

image = Image.open("./horse.jpg")
data = image.load()

for x in range(image.width):
  for y in range(image.height):
    pixel = data[x,y]

    

    data[x,y] = pixel

image.save("./horse.png")
