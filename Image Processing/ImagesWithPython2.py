# Images with python 2

from PIL import Image, ImageFilter

img = Image.open('.\\Pokedex\\pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = filtered_img.convert('L')
# We can show images using show()

filtered_img.show()  # shows the image

# rotating the image

filtered_img.rotate(-90).show()  # argument is the angle, - is clockwise, + is anticlockwise
clockwise_pikachu = filtered_img.rotate(90)
clockwise_pikachu.show()

# resizing the image

resized_pikachu = filtered_img.resize((300, 300))
resized_pikachu.save('.\\resized_pikachu.png', 'png')

# cropping an image
# Image.crop(box = None)
# Returns a rectangular region from this image. The box is a 4-tuple defining the left,
# upper, right and lower pixel coordinate

cropped_pikachu = filtered_img.crop(box=(100, 100, 400, 400))
cropped_pikachu.save('.\\cropped_pikachu.png', 'png')
