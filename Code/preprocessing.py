# basic libraries
import numpy as np
import pandas as pd
import os

# for data set and confusion matrix
import sklearn
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

# for image manipulation 
from PIL import Image

def open_png_pictures(filename:str):
    image = Image.open(filename)
    return np.array(image.getdata()).reshape(3, 50, 50).astype(np.uint8)

def preprocess_training_images(path:str):
    # num = num of classes
    # append all images and labels to seperated lists
    X_total = list()
    y_total = list()

    for patient in range(len(os.listdir(path))):
        dirpath = os.path.join(path, str(patient))
        for label in range(len(dirpath)):
            dirpath = os.path.join(path, str(label))
            print(label)
            for imgname in range(len(dirpath)):
                dirpath = os.path.join(path, str(imgname))
                print(imgname)
                files = os.listdir(dirpath)
                print(len(files))
            #for filename in tqdm(files):
                #print(filename)

            #X_total.append(open_png_pictures(os.path.join(cpath,filename)))
            #y_total.append(f)

    # convert the image list to numpy array
    X_total = np.array(X_total)

    # normalize the arrays to 0 and 1
    X_total = X_total / 255 

    # to_categorical converts an array of labeled data(from 0 to nb_classes-1) to one-hot vector.
    y_total = np_utils.to_categorical(y_total)

    # num_classes for Dense Layer
    num_classes = y_total.shape[1]
    print('num classes:',num_classes)
    
    print("Test example array of the first image: ", X_total[0])
    
    print(f"length X_total: {len(X_total)}")
    print("---------------------------------------------------------------------------------------")
    print(f"length y_total: {len(y_total)}")
    print("---------------------------------------------------------------------------------------")
    
    # randomize the data set
    X_total, y_total = shuffle(X_total, y_total, random_state=0)

    # splitting the data set into training set (75%) and test set (25%)
    X_train, X_test, y_train, y_test = train_test_split(X_total, y_total)
    print("Dimensionen Traindata: ", X_test.ndim)
    
    return (num_classes, X_train, X_test, y_train, y_test)
