# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import plot_model
from keras.models import load_model

import numpy as np
import os,random, sys


if __name__ == "__main__":
    
    classifier = load_model("model/classifier1.h5")
    print("Loaded classifiers from disk")

    test_image = image.load_img('data/animal_test/cat_test/16.png', target_size = (32, 32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    print(result)
    # [[1.00000000e+00 1.33672745e-33]] cat 15
    # [[1.6280557e-08 1.0000000e+00]] cat 16

    # [[1. 0.]] dog 15
    # [[1.000000e+00 7.910713e-38]] dog 16