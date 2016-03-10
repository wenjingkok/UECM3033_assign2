import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import scipy.linalg as linalg

img=mpimg.imread('Lenna.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.savefig('lenna_rgb.jpg')

#Own Image
img2 = mpimg.imread('image.jpg')
[r,g,b] = [img2[:,:,i] for i in range(3)]
fig2 = plt.figure(2)
im1 = fig2.add_subplot(2,2,1)
im2 = fig2.add_subplot(2,2,2)
im3 = fig2.add_subplot(2,2,3)
im4 = fig2.add_subplot(2,2,4)
im1.imshow(img2)
im2.imshow(r, cmap = 'Reds')
im3.imshow(g, cmap = 'Greens')
im4.imshow(b, cmap = 'Blues')
plt.savefig('image_rgb.jpg')

#Calculate SVD for each color
rU, rSigma, rV = linalg.svd(r, full_matrices = True)
gU, gSigma, gV = linalg.svd(g, full_matrices = True)
bU, bSigma, bV = linalg.svd(b, full_matrices = True)

#Lower Resolution Image
lowerImg = img2

rSigmaLow = np.zeros((800, 1000))
gSigmaLow = np.zeros((800, 1000))
bSigmaLow = np.zeros((800, 1000))

for i in range(0, 30):
    rSigmaLow[i][i] = rSigma[i]
    gSigmaLow[i][i] = gSigma[i]
    bSigmaLow[i][i] = bSigma[i]

lowerImg[:,:,0] = np.dot(np.dot(rU, rSigmaLow), rV)
lowerImg[:,:,1] = np.dot(np.dot(gU, gSigmaLow), gV)
lowerImg[:,:,2] = np.dot(np.dot(bU, bSigmaLow), bV)

lowerImg = Image.fromarray(lowerImg,'RGB')
lowerImg.save('lowerResolution.jpg')

#Higher Resolution Image
higherImg = img2

rSigmaHigh = np.zeros((800, 1000))
gSigmaHigh = np.zeros((800, 1000))
bSigmaHigh = np.zeros((800, 1000))

for i in range(0, 800):
    rSigmaHigh[i][i] = rSigma[i]
    gSigmaHigh[i][i] = gSigma[i]
    bSigmaHigh[i][i] = bSigma[i]
    
higherImg[:,:,0] = np.dot(np.dot(rU, rSigmaHigh), rV)
higherImg[:,:,1] = np.dot(np.dot(gU, gSigmaHigh), gV)
higherImg[:,:,2] = np.dot(np.dot(bU, bSigmaHigh), bV)

higherImg = Image.fromarray(higherImg, 'RGB')
higherImg.save('higherResolution.jpg')