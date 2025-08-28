from PIL import Image

image = Image.open("./cobra.jpg")
raster = image.load()

for x in range(image.width):
    for y in range(image.height):
        pixel = raster[x,y]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        
        k = .2 * r + .7 * g + .1 * b
        k = int(k)
        
        if(g > 100):
            pass
        else:        
            # print(pixel)
            raster[x,y] = (k, k, k)

image.save("./cobra_selective_color.png")
