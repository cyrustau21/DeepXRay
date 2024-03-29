import os
from label_reader import LabelReader
import cv2
import numpy as np

class PrepareData:

    def prepare(self,image_dir="images/"):
        image_names = os.listdir(image_dir)

        l = LabelReader()
        annotations = l.read()

        x = []
        y = []

        for name in image_names:
            print(name)
            image = cv2.imread(image_dir+name)
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image,(448,448))
            image = np.expand_dims(image,2)
            x.append(image)
            y.append(self.convert_to_onehot(annotations[name]))

        ids = []
        for i in range(len(x)):
            ids.append(i)

        ids = np.asarray(ids)
        np.random.shuffle(ids)

        x_shuff = []
        y_shuff = []
        for id in ids:
            x_shuff.append(x[id])
            y_shuff.append(y[id])

        x = np.asarray(x_shuff)
        y = np.asarray(y_shuff)

        x = [x]
        y = [y]

        return x,y

    def convert_to_onehot(self,labels):
        y = np.zeros(15)
        for l in labels:
            y[l] = 1
        return np.asarray(y)