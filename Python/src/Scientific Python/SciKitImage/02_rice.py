import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import skimage.measure as measure
import skimage.morphology as morphology
import scipy.ndimage as nd

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)


rice = load_image("images/rice.jpg")
print "Shape of raw image: {}".format(rice.shape)

# algorithms work with monochrome images
rice = rice[:,:,0]
print "Shape of red image: {}".format(rice.shape)
set_title("monchrome image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# enhance the image
rice[ rice[:,:] > 120 ] = 255
rice[ rice[:,:] <= 120 ] = 0
set_title("enhanced image")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()


# close rice grains
rice = morphology.binary_closing(rice)
set_title("after skimage.morphology.binary_closing")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# fill in holes
rice = nd.binary_fill_holes(rice).astype(int)
set_title("after scipy.ndimage.binary_fill_holes")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()



# remove small objects (they must be labelled)
rice = measure.label(rice)
rice = morphology.remove_small_objects(rice)
set_title("after skimage.morphology.remove_small_objects")
plt.imshow(rice, interpolation="none", cmap="gray")
plt.show()

# pick up info on objects
rice = measure.label(rice)
props = measure.regionprops(rice, ['FilledArea', 'Label'])
for item in props:
    b = item['bbox']
    x = (b[0] + b[2])/2
    y = (b[1] + b[3])/2
    n = item['Label']
    message = str(item['Label'])
    plt.text(x, y, message, color="white")
set_title("labelling {} objects".format(len(props)))
plt.imshow(rice, interpolation = "none", cmap = "jet")
plt.show()
