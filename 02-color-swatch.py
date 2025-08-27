from PIL import Image

image = Image.new("RGB", (100, 100))
data = image.load()

for x in range(image.width):
  for y in range(image.height):
    r = int(x/image.width*256)
    g = int(y/image.height*256)
    b = 128

    data[x,y] = (r, g, b)

image.save("./colors.png")
