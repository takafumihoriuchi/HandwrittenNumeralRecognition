## compute.py

import json
import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle
import matplotlib.pylab as plt
from deep_convnet import DeepConvNet

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    
    #get data as an array from read_in()
    lines = read_in()

    #create a numpy array
    np_lines = np.array(lines)
    np_lines = np.delete(np_lines, 784)

    #reshape array to match Convolutional Nueural Network input
    img_reshaped = np_lines.astype(np.float32).reshape(1, 1, 28, 28)
    img_normalized = img_reshaped / 255.0

    network = DeepConvNet()
    network.load_params("deep_convnet_params.pkl")

    y = network.predict(img_normalized)
    p = np.argmax(y)
    print(p)

#start process
if __name__ == '__main__':
    main()