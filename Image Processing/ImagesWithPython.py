from PIL import Image, ImageFilter

img = Image.open('.\\Pokedex\\pikachu.jpg')

print(img)  # We get PIL Object, having the image resolution, format, etc.

print(img.format)  # Format of the image
print(img.size)  # Size/ Resolution of the image
print(img.mode)  # Coloring Mode

print(img.__dir__())

# We can apply filters to the image from Image Filter module which has multiple image filters defined
# We pass the class as an argument to the filter method of the Image class present in the image module.
# The image is passed as self. The filter method calls the passed class and applies the settings onto the image
# Hence we get the filtered image

# Here we are using .png format as filters applied can be saved easily in png
# image.save(directory + name,format) saves the image in the specified location with specified name and format.
# It returns a converted copy
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("smooth.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharp.png", "png")

# image.convert() is a method of image class that converts image from one mode to another. It returns a converted copy
# like RGB -> L(grey)
converted_img = img.convert('L')
converted_img.save("grey.png", "png")

help(filtered_img.convert())
