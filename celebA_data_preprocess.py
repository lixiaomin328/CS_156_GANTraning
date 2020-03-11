import os
import matplotlib.pyplot as plt
from PIL import Image
#from scipy.misc import imresize
import numpy
# root path depends on your computer
root = './data/celeba/img_align_celeba/'
save_root = './data/resized_celebA/'
resize_size = 28

if not os.path.isdir(save_root):
    os.mkdir(save_root)
if not os.path.isdir(save_root + 'celebA'):
    os.mkdir(save_root + 'celebA')
img_list = os.listdir(root)

# ten_percent = len(img_list) // 10

for i in range(len(img_list)-28000):
    img = Image.open(root + img_list[i])
    newImage = img.resize((resize_size,resize_size))
    #img = imresize(img, (resize_size, resize_size))
    plt.imsave(fname=save_root + 'celebA/' + img_list[i], arr=newImage)

    if (i % 1000) == 0:
        print('%d images complete' % i)
