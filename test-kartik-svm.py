import ml
import numpy as np

dir_path = './final/kartik/'

train = ml.AudioFeatures().extract(filename=dir_path + 'final-train')
test = ml.AudioFeatures().extract(filename=dir_path + 'final-test')

def labels_to_class(labels):
    temp = []
    for i in range(0, len(labels)):
        if labels[i][0] == 1:
            temp.append(0)
        elif labels[i][1] == 1:
            temp.append(1)
    return temp

train.class_labels = np.array(labels_to_class(train.labels))
test.class_labels = np.array(labels_to_class(test.labels))

svm = ml.SVM(features_dim=21, classes=2, svm_type='c', kernel='poly', poly_degree=3)
print svm

svm.train(train=train, test=test)

