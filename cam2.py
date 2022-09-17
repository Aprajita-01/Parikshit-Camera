import flirpy
from flirpy import camera
from flirpy.camera import tau,tau_config
from flirpy.camera.tau import Tau
import cv2
import numpy as np
import serial
import matplotlib.pyplot as plt

camera = Tau('COM6', 921600)

'''erase_snapshots gives a blank output. Need to reset camera through gui afterwards.'''

count = 0
while count<1:
    try:
        camera.snapshot(0)
        number,size=camera.get_num_snapshots()
        print("Number of snapshots: {0} " .format(number))
        print("Size of snapshots: {0} ".format(size))
        image = camera.retrieve_snapshot(number-1)
        image = image[:327680]
        image = np.reshape(image, (512, 640))
        plt.imshow(image)
        plt.show()
        count = count+1
    except:continue
        
