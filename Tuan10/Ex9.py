import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image


im=Image.open("./lena.jpg").convert("L")
im_g=np.asarray(im)

U,S,V=np.linalg.svd(im_g,full_matrices=True)
S=np.diag(S)

for r in range(0,300,50):
    R=U[:,:r]@S[:r,:r]@V[:r,:]
    plt.imshow(R,cmap="gray")
    plt.title(f"SVD with {r} singular values")
    plt.pause(0.05)
    plt.plot()
    plt.clf()
    R=R.astype(np.uint8)
    compressed_img=Image.fromarray(R)
    compressed_img.save(f"SVD_compressed_{r}.jpg")