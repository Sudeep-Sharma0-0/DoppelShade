from PIL import Image


def doppeler():

    image = Image.open("./images/mona_lisa.webp")
    image.thumbnail((100, 100))
    pixels = image.load()

    def pixel_to_shadow(pixel, x, y):
        string = f"{(x+1)*5}px {(y)*5}px 3px 2px rgba{pixel}"
        return string

    shadows = "div {\n\tbox-shadow:\n"
    for y in range(image.height):
        for x in range(image.width):
            shadows += pixel_to_shadow(pixels[x, y], x, y)
            last_line = x == image.width - 1 and y == image.height - 1
            shadows += ";\n" if last_line else ",\n"
    shadows += "}"
    with open("./html/style.css", "w") as file:
        file.write(shadows)
        print(file)
