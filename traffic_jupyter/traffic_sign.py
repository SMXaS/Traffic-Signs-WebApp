"""Importing libraries"""
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
import matplotlib.pyplot as plt

"""Storing data and labels in the list"""
data = []
labels = []

"""Locating working directory and printing it out"""
file_path = os.getcwd()
print(file_path)

"""
Looping through 43 classes
Opening data - train file
Declaring 'images' as faster way to open train file
---------------------------------------------------
Looping through settings of images
Opening images
Resizing the pictures
Modifying the list with append for data and labels
Raising the exception if there was any errors
"""
for pictures in range(43):
    data_path = os.path.join(file_path, 'Data/Train', str(pictures))
    images = os.listdir(data_path)
    for setting in images:
        try:
            image = Image.open(data_path + '//' + setting)
            image = image.resize((30, 30))
            image = np.array(image)
            data.append(image)
            labels.append(pictures)
        except Exception as error:
            print(error)

"""Making data and labels list to be numpy arrays"""
data = np.array(data)
labels = np.array(labels)

"""
Making a folder for model
Saving model after training
The model can be used and no need to be trained
"""
#os.mkdir('Saved_model')
np.save('./Saved_model/data', data)
np.save('./Saved_model/labels', labels)

"""Loading model"""
#data = np.load('./Saved_model/data.npy')
#labels = np.load('./Saved_model/labels.npy')

"""Printing out the shape of data and labels"""
print(data.shape, labels.shape)

"""Preparing testing, training and setting up the parameters"""
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=0)

"""Printing the shape"""
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""Converting classes to encoded data"""
y_train = to_categorical(y_train, 43)
y_test = to_categorical(y_test, 43)

"""
Preparing the model
Model has parameters from KERAS API
Activation layers for model
"""
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5, 5), activation='relu', input_shape=X_train.shape[1:]))
model.add(Conv2D(filters=32, kernel_size=(5, 5), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.25))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(rate=0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(43, activation='softmax'))

"""Compiling the model"""
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

"""Setting up the epochs and history of each compile"""
epochs = 20
history = model.fit(X_train, y_train, batch_size=32, epochs=epochs, validation_data=(X_test, y_test))

"""Printing the MATLAB diagram of the trained data"""
plt.figure(0)
plt.plot(history.history['accuracy'], label='training accuracy')
plt.plot(history.history['val_accuracy'], label='val accuracy')
plt.title('Accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()

"""Printing the MATLAB diagram of loss accuracy"""
plt.plot(history.history['loss'], label='training loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.title('Loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

"""Reading csv file..."""
def testing(testcsv):
    y_test = pd.read_csv(testcsv)
    label = y_test["ClassId"].values
    imgs = y_test["Path"].values
    data = []
    for img in imgs:
        image = Image.open(img)
        image = image.resize((30, 30))
        data.append(np.array(image))
    X_test = np.array(data)
    return X_test, label

"""Declaring the file"""
X_test, label = testing('Test.csv')

"""Running prediction function for the test"""
Y_pred = model.predict_classes(X_test)
Y_pred

"""Printing accuracy from the testing"""
from sklearn.metrics import accuracy_score
print(accuracy_score(label, Y_pred))

"""Saving the model"""
model.save("./home/wu/Desktop/Final project/Saved_model/model.h5")

"""Loading the model"""
import os
os.chdir(r'/home/wu/Desktop/Final project')
from keras.models import load_model
model = load_model("./Saved_model/model.h5")

"""Classes for predicting"""
classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)', 
            2:'Speed limit (50km/h)', 
            3:'Speed limit (60km/h)', 
            4:'Speed limit (70km/h)', 
            5:'Speed limit (80km/h)', 
            6:'End of speed limit (80km/h)', 
            7:'Speed limit (100km/h)', 
            8:'Speed limit (120km/h)', 
            9:'No passing', 
            10:'No passing veh over 3.5 tons', 
            11:'Right-of-way at intersection', 
            12:'Priority road', 
            13:'Yield', 
            14:'Stop', 
            15:'No vehicles', 
            16:'Veh > 3.5 tons prohibited', 
            17:'No entry', 
            18:'General caution', 
            19:'Dangerous curve left', 
            20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons' }

"""
Importing libararies
Defining a function that will open the image
Image will be resized with testing
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def test_on_img(img):
    data=[]
    image = Image.open(img)
    image = image.resize((30, 30))
    data.append(np.array(image))
    X_test = np.array(data)
    Y_pred = model.predict_classes(X_test)
    return image, Y_pred

"""Delcaring the image to recognize"""
plot,prediction = test_on_img(r'/home/wu/Desktop/Final project/Data/Test/00000.png')
class_string = [str(i) for i in prediction]
class_number = int("".join(class_string))
print("Predicted traffic sign is: ", classes[class_number])
plt.imshow(plot)
plt.show()