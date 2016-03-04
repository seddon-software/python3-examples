import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import skimage.morphology as morphology
import skimage.feature as feature
import PIL.Image as Image

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

# # use PIL to show true image
# from PIL import Image
# img = Image.open("images/tablets.jpg")    
# img.show()

# image is an int numpy array [0 ... 255] 
set_title("numpy int array 0 ... 255")
image = load_image("images/tablets.jpg")
plt.imshow(image, interpolation="none")
plt.show()


# convert image to floats
image = image / 256.0
set_title("numpy float array 0.0 ... 1.0")
plt.imshow(image, interpolation="none")
plt.show()

# algorithms expect monochrome images
# so just use the RED part of the image
image = image[:,:,0]

# use Canny algorith to detect edges
# vary sigma
for i in range(2,10):
    set_title("sigma = {}".format(i))
    edges = feature.canny(image, sigma=i, low_threshold=40/256.0, high_threshold=50/256.0)
    plt.imshow(edges, cmap=plt.cm.gray)
    plt.show()

# vary thresholds
for i in range(5, 60, 5):
    low = i / 256.0
    high = (i + 5) / 256.0
    set_title("low = {}, high = {}".format(low*256, high*256))
    edges = feature.canny(image, sigma=4, low_threshold=low, high_threshold=high)
    plt.imshow(edges, cmap=plt.cm.gray)
    plt.show()

# chose best parametrs
sigma = 4
low = 40/256.0
high = 45/256.0
set_title("Best choice: sigma = {}, low = {}, high = {}".format(sigma, low*256, high*256))
edges = feature.canny(image, sigma=sigma, low_threshold=low, high_threshold=high)

# close edges
for i in range(1,10):
    closed = morphology.binary_closing(edges, morphology.square(i)).astype(int)
    # fill circles
    set_title("fill factor = {}".format(i))
    filled = nd.binary_fill_holes(closed).astype(int)
    plt.imshow(filled, cmap=plt.cm.gray)
    plt.show()




