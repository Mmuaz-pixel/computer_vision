import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

#  Arguments of calcHist function 

'''
images: This is the source image, and it should be given in square brackets ([img]). You can pass a single image or a list of images (e.g., [img1, img2]) if you want to compute histograms for multiple images. Each image can have multiple channels.

channels: This specifies the channel or channels for which you want to compute the histogram. It is also given in square brackets. For a grayscale image, it should be [0]. For a color image, you can compute separate histograms for each channel, and channels would be [0] for blue, [1] for green, and [2] for red.

mask: A mask image. To compute the histogram for the entire image, it is set to None. If you want to compute the histogram for a specific region of interest, you can provide a mask image where the histogram will be calculated only for non-zero pixels.

histSize: This is the number of bins for the histogram. For grayscale images, it is an integer representing the number of bins. For color images, you need to specify it for each channel, so histSize would be [histSize1, histSize2, histSize3].

ranges: This represents the range of pixel values you want to consider in the histogram. For grayscale images, it is usually [0, 256] as pixel values range from 0 to 255. For color images, you need to specify the range for each channel like [[0, 256], [0, 256], [0, 256]]

'''

img = cv.imread('image.jpg')

colors = ('blue', 'green', 'red')

for i, col,  in enumerate(colors): 
    number_of_bins = 50
    hist = cv.calcHist([img], [i], None, [number_of_bins], [0, 256])
    bin_edges = np.linspace(0, 256, number_of_bins+1)  # bins from 0 to 256
    plt.plot(bin_edges[:-1], hist.flatten(), color=col)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

plt.show()