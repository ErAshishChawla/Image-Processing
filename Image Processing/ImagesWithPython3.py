# Images with Python 3

from PIL import Image, ImageFilter

img = Image.open('.\\astro.jpg')
print(img.size)

resized_img = img.resize((400, 400))  # Tuple is (width,height)
resized_img.save('.\\astro_thumbnail.jpeg', 'JPEG')

# when we resize the image to completely different resolution. Then its aspect ratio(w/h) is
# lost. Image feels compressed.

# to save the aspect ratio. We use .thumbnail((w,h))
# .thumbnail is a method that changes the original image

img.thumbnail((400, 400))
img.save('.\\astro_thumbnail_2.jpeg', 'jpeg')

# This method tries its best to maintain the aspect ratio.
# So, in this process it is possible that this may not lead to the exact specified
# dimensions
